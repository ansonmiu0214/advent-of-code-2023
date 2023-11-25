#!/usr/bin/env sh

set -e

if [[ "$#" != 3 ]]; then
    echo "usage: $0 <day> <part> <input_type>"
    exit 1
fi

DAY=$1
PART=$2
INPUT_TYPE=$3

PART_NUMBER=${PART#"part"}
python -m aoc.solutions.$DAY --day $DAY --part $PART_NUMBER --input-type $INPUT_TYPE