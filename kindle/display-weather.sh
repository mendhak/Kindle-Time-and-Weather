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

if wget -O weather-script-output.png http://time.mendhak.com; then
	eips -g weather-script-output.png
else
	eips -g weather-image-error.png
fi
