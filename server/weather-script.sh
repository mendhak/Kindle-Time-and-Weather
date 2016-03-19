#!/bin/sh

cd "$(dirname "$0")"


if [ ! -d pngcrush-1.7.67 ]
then
  echo "Seem to be missing pngcrush-1.7.67 in "$(pwd)
  #exit 1
fi


date

echo "------ python get data from metoffice"
python weather-script.py

echo "------ convert to png"
convert -rotate 270 -resize 758x1024\!  -depth 8 weather-script-output.svg weather-script-output.png

echo "------ shrink png"
pngcrush  -q -c 0 weather-script-output.png weather-script-output_s.png

echo "------ copy to webserver"
cp -f weather-script-output_s.png /www/root/weather-script-output.png
