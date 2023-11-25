#!/usr/bin/env sh

set -e

DAY=$1
PART=$2
INPUT_TYPE=$3

SOURCEDIR="/workarea"
BUILDDIR="/buildarea"

cd $BUILDDIR
cmake -DCMAKE_CXX_FLAGS="-stdlib=libc++" $SOURCEDIR
make $DAY

EXE="$BUILDDIR/aoc/$DAY"
$EXE --day $DAY --part $PART --input-type $INPUT_TYPE