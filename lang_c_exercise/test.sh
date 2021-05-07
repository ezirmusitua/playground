#!/usr/bin/bash

NAME=$1

if [[ "$NAME" == "" ]]; then
  echo "Invalid NAME"
  exit -1
fi

# if [[ ! -z gcc ]]; then
#   echo "gcc not found"
#   exit -1
# fi
gcc "./src/$NAME.c" -o "./build/$NAME"

./build/$NAME