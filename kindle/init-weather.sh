#!/bin/sh

/etc/init.d/framework stop
/etc/init.d/powerd stop
#Hides the status bar (aka pillow)
/mnt/us/weather/utils/hide-top-bar
#Prevent the Kindle from sleeping
/mnt/us/weather/utils/prevent-ss
#Don't make it toooo bright
./set-brightness 13
#Do the actual image download and setting
/mnt/us/weather/display-weather.sh
