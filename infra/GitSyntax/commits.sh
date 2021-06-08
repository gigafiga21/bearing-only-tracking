#!/bin/sh

# Checks git commit naming style
# {String} $1 - commit message to check
function checkCommitStyle {
    # Checking commit syntax 
    TEST=`echo "$MESSAGE" | sed -n '/^[A-Z].* (issue #[0-9]*)\.$/p'`;

    if [[ $TEST == "" ]]; then
        printf "\nerror: invalid commit syntax."
        printf "\n\n  Valid syntax is \"Commit message (issue #[issue id]).\" \n\n"
        return 1;
    fi

    return 0;
}
