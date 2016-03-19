#!/bin/sh

cd "$(dirname "$0")"

rm weather-script-output.png
eips -c
eips -c

#Once an hour, clear the screen a bit

ifStart=`date '+%M'`
if [ $ifStart == 22 ]
then
  eips -q
  eips -p
fi

if wget http://192.168.1.91:9000/weather-script-output.png; then
	eips -g weather-script-output.png
else
	eips -g weather-image-error.png
fi
