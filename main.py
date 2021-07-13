import sys
sys.path.append("./source")

import math
from functools import reduce
from matplotlib import pyplot
from argparse import ArgumentParser
from source.modules.Loader.main import Loader
from source.modules.Converter.main import Converter
from source.modules.Tracer.main import Tracer
from source.modules.Measurer.main import Measurer
from source.modules.ManeuverDetector.main import ManeuverDetector
from source.modules.MotionCalculator.main import MotionCalculator
from source.modules.Plotter.main import Plotter

def convert(conversionType, inputFile, outputFile):
    converted = []
    if conversionType == "pc":
        converted = Converter.polToCart(Loader.read(inputFile, Loader.polar))
        Loader.write(outputFile, converted, Loader.headerCartesian)
    elif conversionType == "cp":
        converted = Converter.cartToPol(Loader.read(inputFile, Loader.cartesian))
        Loader.write(outputFile, converted, Loader.headerPolar)

def distancesCommon(inputObserver, inputTarget, bearingPeriod, sigma = 0):
    bearingPeriod = 20 if bearingPeriod is None else bearingPeriod

    routeObserver = Tracer.trace(Loader.read(inputObserver, Loader.polar), bearingPeriod)
    routeObserverCart = Converter.polToCart(routeObserver)
    routeTarget = Tracer.trace(Loader.read(inputTarget, Loader.polar), bearingPeriod)
    routeTargetCart = Converter.polToCart(routeTarget)
    bearings = Measurer.addNoise(Measurer.bearings(routeObserver, routeTarget), sigma)

    maneuverIndex = 0
    maneuverLength = 0
    prevManeuverIndex = 0
    params = []
    distances = []
    maneuverDistance = {}

    for i in range(3, len(bearings)):
        isManeuver = ManeuverDetector.detect(bearings[i - 3:i + 1], sigma)
        if maneuverIndex + 3 == i:
            manueverEnd = maneuverIndex #+ maneuverLength
            maneuverLength = 0
            params.append(MotionCalculator.getParams(
                3,
                bearingPeriod,
                bearings[manueverEnd],
                bearings[manueverEnd + 1],
                bearings[manueverEnd + 3]
            ))
            if len(params) > 2:
                lastParams = len(params) - 1
                maneuverDistance = {
                    "time": routeObserver[maneuverIndex]["time"],
                    "d": MotionCalculator.maneuverDistance(params[lastParams - 1], params[lastParams], routeObserver[i - 3]["speed"], routeObserver[i - 3]["yaw"], bearings[maneuverIndex + math.floor(maneuverLength / 2)]),
                    "bearing": bearings[maneuverIndex + math.floor(maneuverLength / 2)],
                    "observer": routeObserverCart[maneuverIndex + math.floor(maneuverLength / 2)]
                }
                distances.append(maneuverDistance)
                print(
                    "\nCalculated target maneuver time start: ", routeObserver[maneuverIndex]["time"],
                    "\nCalculated target maneuver time end: ", routeObserver[manueverEnd]["time"],
                    "\nError of detecting distance between objects: ", - maneuverDistance["d"] + Measurer.distances(routeTargetCart, routeObserverCart)[maneuverIndex]["d"]
                )
        
        if isManeuver:
            if maneuverIndex + maneuverLength + 2 == i:
                maneuverLength += 1
            else:
                maneuverIndex = i - 1
                maneuverLength = 0
        elif maneuverIndex + maneuverLength + 3 == i:
            if len(params) > 0:
                lastParams = len(params) - 1
                params.append(MotionCalculator.recalculateParams(
                    params[lastParams]["alpha"],
                    params[lastParams]["beta"],
                    routeObserver[maneuverIndex - 1]["time"] - routeObserver[prevManeuverIndex]["time"],
                ))
                prevManeuverIndex = maneuverIndex

        if len(distances) > 0 and not isManeuver and maneuverIndex + maneuverLength + 3 <= i:
            distances.append({
                "time": routeObserver[i]["time"],
                "d": MotionCalculator.linearDistance(
                    [routeObserverCart[maneuverIndex]] + Converter.toRelative(routeObserverCart[i - 1:i + 1], routeObserverCart[maneuverIndex]),
                    [bearings[maneuverIndex], *bearings[i - 1:i + 1]],
                    maneuverDistance["d"]
                )["d"],
                "bearing": bearings[i],
                "observer": routeObserverCart[i]
            })

    Plotter.routes([routeTargetCart, routeObserverCart, Converter.radiusToCart(distances)])
    Plotter.figure()
    Plotter.distances([
        Measurer.distances(routeTargetCart, routeObserverCart),
        distances
    ])
    Plotter.figure()
    Plotter.deltaBearings(list(map(lambda p: p["time"], routeObserver)), bearings)
    Plotter.show()

def distancesLinear(inputObserver, inputTarget, bearingPeriod, sigma = 0):
    bearingPeriod = 20 if bearingPeriod is None else bearingPeriod

    routeObserver = Tracer.trace(Loader.read(inputObserver, Loader.polar), bearingPeriod)
    routeObserverCart = Converter.polToCart(routeObserver)
    routeTarget = Tracer.trace(Loader.read(inputTarget, Loader.polar), bearingPeriod)
    routeTargetCart = Converter.polToCart(routeTarget)
    bearings = Measurer.addNoise(Measurer.bearings(routeObserver, routeTarget), sigma)

    distances = [{
        "time": routeObserver[0]["time"],
        "d": Measurer.addNoise([Measurer.distance(routeTargetCart[0], routeObserverCart[0])["d"]], 1800),
        "bearing": bearings[0],
        "observer": routeObserverCart[0]
    }]

    for i in range(2, len(bearings)):
        targetParams = MotionCalculator.linearDistance(
            routeObserverCart[0:i + 1],
            bearings[0:i + 1],
            distances[0]["d"]
        )
        distances.append({
            "time": routeObserver[i]["time"],
            "d": targetParams["d"],
            "bearing": bearings[i],
            "observer": routeObserverCart[i]
        })
    
    Plotter.routes([routeTargetCart, routeObserverCart, Converter.radiusToCart(distances)])
    Plotter.figure()
    Plotter.distances([
        Measurer.distances(routeTargetCart, routeObserverCart),
        distances
    ])
    Plotter.show()


# CLI interface
parser = ArgumentParser()
parser.add_argument("-d", "--distance", dest="isDistance",
    help="distance computational mode; requires `--observer` and `--target` arguments;", action="store_true", default=False)
parser.add_argument("-dl", "--distance-linear", dest="isLinearDistance",
    help="distance on linear path computational mode; requires `--observer` and `--target` arguments;", action="store_true", default=False)
parser.add_argument("-oo", "--observer", dest="observerInput",
    help="a csv table with observer object route points descriptions;", metavar="FILE")
parser.add_argument("-ot", "--target", dest="targetInput",
    help="a csv table with target object route points descriptions;", metavar="FILE")
parser.add_argument("-p", "--period", dest="bearingPeriod",
    help="period of the finding bearings to the target object;", type=int)
parser.add_argument("-s", "--sigma", default=0, dest="sigma",
    help="noise root mean square in degrees;", type=float)
parser.add_argument("-c", "--convert", dest="convert",
    help="`pc` for polar to cartesian conversion, `cp` for cartesian to polar conversion; requires `--input` file with coordinates to convert and `--output` file arguments;", metavar="string")
parser.add_argument("-i", "--input", dest="input",
    help="path to input file;", metavar="FILE")
parser.add_argument("-o", "--output", dest="output",
    help="path to output file;", metavar="FILE")
args = parser.parse_args()

if not (args.convert is None):
    if not (args.convert in ["pc", "cp"]):
        print("ERROR: `--convert` argument can contain `cp` or `pc` values only")
        sys.exit()
    if (args.input is None) or (args.output is None):
        print("ERROR: `--convert` requires both `--input` and `--output` arguments")
        sys.exit()
    convert(args.convert, args.input, args.output)
elif args.isDistance or args.isLinearDistance:
    if (args.observerInput is None) or (args.targetInput is None):
        print("ERROR: `--distance` and `--linear` modes require both `--target` and `--observer` arguments")
        sys.exit()
    if args.isDistance:
        distancesCommon(args.observerInput, args.targetInput, args.bearingPeriod, args.sigma * 180 / math.pi)
    else:
        distancesLinear(args.observerInput, args.targetInput, args.bearingPeriod, args.sigma * 180 / math.pi)
else:
    print("WARNING: nothing to do, consider passing `--distance` or `--convert` flag")
