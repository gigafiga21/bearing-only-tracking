#!/bin/sh

# Prints syntax error
# {String} $1 - error string
function error {
    printf "error: invalid branch syntax.\n";
    printf "error: "$1".";
    printf "\n\n  Valid syntax is \"nickname.issue-description.issue-id\", where:\n";
    printf "  {string} nickname - your nickname on github\n";
    printf "  {string} issue-description - one-word task description\n";
    printf "  {number} issue-id - see on github\n\n";
}

# Checks current git branch naming style
# {Boolean} $1 - loaded in CI or not
function checkBranchStyle {
    BRANCH="";

    # Getting pushing branch name
    if [[ $1 == false ]]; then
        BRANCH=`git rev-parse --abbrev-ref HEAD`;
    elif [[ ! $TRAVIS_PULL_REQUEST_BRANCH == "" ]]; then
        BRANCH=$TRAVIS_PULL_REQUEST_BRANCH;
    fi
    printf "log: checking "$BRANCH"...\n"

    # If master, or launched in CI, but not in PR - return
    if [[ $BRANCH == "master" || $BRANCH == "" ]]; then
        return 0;
    fi

    # Popping info from branch name
    # Splitting string by . into array
    INFO=(${BRANCH//./ });

    # Check if name written in dashed text style (- instead of \s)
    DASHED_TEST=`echo "$BRANCH" | sed -n '/^[a-z,0-9,\.,-]*$/p'`;

    if [[ $DASHED_TEST == "" ]]; then
        error "expected dashed text style without uppercase";
        return 1;
    fi

    if [[ "${1}" == false ]]; then
        # Check if author name in branch match current git user
        AUTHOR=`git config --get user.name`;

        if [[ ! $AUTHOR == ${INFO[0]} ]]; then
            error "author in branch name does not match current author - "${INFO[0]}" vs "$AUTHOR"";
            return 2;
        fi
    fi

    # Check last element in INFO type - must be number (issue id)
    ISSUE_INDEX=$(awk "BEGIN{print "${#INFO[@]}"-1}")
    ISSUE=`echo "${INFO[$ISSUE_INDEX]}" | sed -n '/^[0-9].*$/p'`;

    if [[ ISSUE == "" ]]; then
        error "issue is not mentioned";
        return 3;
    fi

    return 0;
}
