#!/bin/sh

cd "$(dirname "$0")"

rm weather-script-output.png
eips -c
eips -c

if wget http://server:3000/weather-script-output.png; then
	eips -g weather-script-output.png
else
	eips -g weather-image-error.png
fi
