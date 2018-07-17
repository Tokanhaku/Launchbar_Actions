#!/bin/zsh
#
# LaunchBar Action Script
#

export name=`whoami`
export PUBLIC_IP=$name@`curl --fail --silent --show-error ipinfo.io/ip`
echo $PUBLIC_IP | pbcopy
export a='display in notification center "'
export b='" with title "IP Adress Copied!"'
export c=$a$PUBLIC_IP$b
osascript -e 'tell application "LaunchBar"' -e $c -e 'end tell'