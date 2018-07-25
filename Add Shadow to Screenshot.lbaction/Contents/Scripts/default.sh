#!/bin/sh
#
# LaunchBar Action Script
#

echo "$# arguments passed"
for ARG in "$@"; do
    ./shadow "$ARG"
done
