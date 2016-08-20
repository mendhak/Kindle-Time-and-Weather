#!/usr/bin/python

# Kindle Weather Display
# Matthew Petroff (http://www.mpetroff.net/)
# September 2012
#
# Owen Bullock - UK Weather - MetOffice - Aug 2013
# Apr 2014 - amended for Wind option
#
# Mendhak - redone for WeatherUnderground API

import json
import urllib2
from xml.dom import minidom
import datetime
import codecs
import os.path
import time
import sys
import os

#
# Weather Underground API Key - unique to me. 
#
wuapikey= os.environ.get('WUNDERGROUND_API_KEY') or "2f1126aef047991e"


template = 'weather-script-preprocess_temps.svg'

#
#  Map the Wunderground weather codes to Icons.
# ( See https://www.wunderground.com/weather/api/d/docs?d=resources/icon-sets&MR=1 )
#
mapping = [
[0 , 'skc     '],  #  Clear night                     skc.svg
[1 , 'skc     '],  #  Sunny day                       skc.svg
[2 , 'sct     '],  #  Partly cloudy (night)           sct.svg
[3 , 'sct     '],  #  Partly cloudy (day)             sct.svg
[4 , '        '],  #  Not used                        -
[5 , 'fg      '],  #  Mist                            fg.svg
[6 , 'fg      '],  #  Fog                             fg.svg
[7 , 'bkn     '],  #  Cloudy                          bkn.svg
[8 , 'ovc     '],  #  Overcast                        ovc.svg
[9 , 'hi_shwrs'],  #  Light rain shower (night)       hi_shwrs.svg
[10, 'hi_shwrs'],  #  Light rain shower (day)         hi_shwrs.svg
[11, 'hi_shwrs'],  #  Drizzle                         hi_shwrs.svg
[12, 'ra1     '],  #  Light rain                      ra1.svg
[13, 'ra      '],  #  Heavy rain shower (night)       ra.svg
[14, 'ra      '],  #  Heavy rain shower (day)         ra.svg
[15, 'ra      '],  #  Heavy rain                      ra.svg
[16, 'rasn    '],  #  Sleet shower (night)            rasn.svg
[17, 'rasn    '],  #  Sleet shower (day)              rasn.svg
[18, 'rasn    '],  #  Sleet                           rasn.svg
[19, 'ip      '],  #  Hail shower (night)             ip.svg
[20, 'ip      '],  #  Hail shower (day)               ip.svg
[21, 'ip      '],  #  Hail                            ip.svg
[22, 'sn      '],  #  Light snow shower (night)       sn.svg
[23, 'sn      '],  #  Light snow shower (day)         sn.svg
[24, 'sn      '],  #  Light snow                      sn.svg
[25, 'sn      '],  #  Heavy snow shower (night)       sn.xvg
[26, 'sn      '],  #  Heavy snow shower (day)         sn.svg
[27, 'sn      '],  #  Heavy snow                      sn.svg
[28, 'tsra    '],  #  Thunder shower (night)          tsra.svg
[29, 'tsra    '],  #  Thunder shower (day)            tsra.svg
[30, 'tsra    '],  #  Thunder                         tsra.svg
]

icon_dict={
'chanceflurries':'sn',
'chancerain':'hi_shwrs',
'chancesleet':'rasn',
'chancesnow':'sn',
'chancetstorms':'tsra',
'clear':'skc',
'cloudy':'bkn',
'flurries':'sn',
'fog':'fg',
'hazy':'fg',
'mostlycloudy':'ovc',
'mostlysunny':'skc',
'partlycloudy':'sct',
'partlysunny':'skc',
'sleet':'rasn',
'rain':'ra',
'sleet':'rasn',
'snow':'sn',
'sunny':'skc',
'tstorms':'tsra',
'cloudy':'bkn',
'partlycloudy':'bkn',

}

#
# Download and parse weather data - location 353773 = Sutton, Surrey
#

weather_json=''
stale=True

if(os.path.isfile(os.getcwd() + "/wunderground.json")):
    #Read the contents anyway
    with open(os.getcwd() + "/wunderground.json", 'r') as content_file:
        weather_json = content_file.read()
    stale=time.time() - os.path.getmtime(os.getcwd() + "/wunderground.json") > (12*60*60)

#If old file or file doesn't exist, time to download it
if(stale):
    try:
        print "Old file, attempting re-download"
        url='http://api.wunderground.com/api/' + wuapikey + '/forecast/q/UK/Reigate.json'
        weather_json = urllib2.urlopen(url).read()
        with open(os.getcwd() + "/wunderground.json", "w") as text_file:
            text_file.write(weather_json)
    except:
        print "FAILED. using previous read"
        with open(os.getcwd() + "/wunderground.json", 'r') as content_file:
            weather_json = content_file.read()

weatherData = json.loads(weather_json)
icon_one = weatherData['forecast']['simpleforecast']['forecastday'][0]['icon']
high_one = weatherData['forecast']['simpleforecast']['forecastday'][0]['high']['celsius']
low_one  = weatherData['forecast']['simpleforecast']['forecastday'][0]['low']['celsius']
day_one  = weatherData['forecast']['simpleforecast']['forecastday'][0]['date']['weekday']

icon_two = weatherData['forecast']['simpleforecast']['forecastday'][1]['icon']
high_two = weatherData['forecast']['simpleforecast']['forecastday'][1]['high']['celsius']
low_two  = weatherData['forecast']['simpleforecast']['forecastday'][1]['low']['celsius']
day_two  = weatherData['forecast']['simpleforecast']['forecastday'][1]['date']['weekday']

icon_three = weatherData['forecast']['simpleforecast']['forecastday'][2]['icon']
high_three = weatherData['forecast']['simpleforecast']['forecastday'][2]['high']['celsius']
low_three  = weatherData['forecast']['simpleforecast']['forecastday'][2]['low']['celsius']
day_three  = weatherData['forecast']['simpleforecast']['forecastday'][2]['date']['weekday']


print icon_one,low_one,high_one,day_one
print icon_two,low_two,high_two,day_two
print icon_three,low_three,high_three,day_three



dtnow=datetime.datetime.now().strftime("%d-%b %H:%M")
print "NOW:",dtnow


#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open(template , 'r', encoding='utf-8').read()

# Insert weather icons and temperatures
output = output.replace('ICON_ONE',icon_dict[icon_one])
output = output.replace('ICON_TWO',icon_dict[icon_two])
output = output.replace('ICON_THREE',icon_dict[icon_three])

output = output.replace('TIME_NOW',datetime.datetime.now().strftime("%H:%M"))


output = output.replace('HIGH_ONE',high_one)
output = output.replace('HIGH_TWO',high_two)
output = output.replace('HIGH_THREE',high_three)


output = output.replace('LOW_ONE',low_one)
output = output.replace('LOW_TWO',low_two)
output = output.replace('LOW_THREE',low_three)


# Insert current time
# (thanks Jennifer http://www.shatteredhaven.com/2012/11/1347365-kindle-weather-display.html)
output = output.replace('DATE_VALPLACE',str(dtnow))
readableDate = datetime.datetime.now().strftime("%A %B %d")
output = output.replace('TODAY_DATE', str(readableDate))

output = output.replace('DAY_TWO',day_two)
output = output.replace('DAY_THREE',day_three)

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)

