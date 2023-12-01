#!/usr/bin/env sh
#
# Build and run the solution for a given part of a given day's problem,
# using a given type of input file.

set -e

if [[ "$#" != 4 ]]; then
    echo "usage: $0 LANGUAGE DAY PART INPUT_TYPE"
    echo
    echo "arguments:"
    echo "  LANGUAGE     the programming language"
    echo "  DAY          the day of a problem, day{01..25}"
    echo "  PART         the part of a problem, part{1,2}"
    echo "  INPUT_TYPE   type of input file, {sample,test}"
    exit 1
fi

# Parse and validate arguments.

LANG=$1

ROOTDIR=$(realpath "$0/..")
DATADIR="$ROOTDIR/data"
LANGDIR="$ROOTDIR/drivers/$LANG"

if [[ ! -d "$LANGDIR" ]]; then
    echo "No directory for language: $LANG"
    exit 1
fi

if [[ ! -f "$LANGDIR/run.sh" ]]; then
    echo "No 'run.sh' driver for language: $LANG"
    exit 1
fi

DAY=$2
if [[ ! "$DAY" =~ ^day..$ ]]; then
    echo "Invalid day supplied: $DAY"
    exit 1
fi

PART=$3
if [[ "$PART" != "part1" ]] && [[ "$PART" != "part2" ]]; then
    echo "Invalid part supplied: $PART"
    exit 1
fi

INPUT_TYPE=$4

shift

IMAGE="advent-of-code-2023:$LANG"

docker build -t $IMAGE $LANGDIR
docker run --rm -it -v $LANGDIR:/workarea -v $DATADIR:/data $IMAGE ./run.sh "$@"