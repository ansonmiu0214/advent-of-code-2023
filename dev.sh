#!/usr/bin/env sh
#
# Launch a container for developing the solution for the specified language.

set -e

if [[ "$#" != 1 ]]; then
    echo "usage: $0 LANGUAGE"
    echo
    echo "arguments:"
    echo "  LANGUAGE     the programming language"
    exit 1
fi

# Parse and validate arguments.

LANG=$1

ROOTDIR=$(realpath "$0/..")
DATADIR="$ROOTDIR/data"
LANGDIR="$ROOTDIR/drivers/$LANG"

if [[ ! -d "$LANGDIR" ]]; then
    echo "No driver for language: $LANG"
    exit 1
fi

IMAGE="advent-of-code-2023:$LANG"

docker build -t $IMAGE $LANGDIR
docker run --rm -it -v $LANGDIR:/workarea -v $DATADIR:/data $IMAGE