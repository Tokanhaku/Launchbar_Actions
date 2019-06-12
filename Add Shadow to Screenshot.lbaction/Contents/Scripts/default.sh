#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"
for ARG in "$@"; do
    ./dropshadow "$ARG"
done
