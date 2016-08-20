
# Kindle Time and Weather

Something you can do with an old Kindle - shows time and weather.  Weather data comes from Weather Underground API.


![](screenshot.png)

Similar to the [original weather display](http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/), but with time and a Docker container.

## Server side

In the server directory, build the image and run it

    sudo docker-compose up -d

Wait a minute or so, and the image should become available at port 9000, like http://localhost:9000/weather-script-output.png

You can change the port in the `docker-compose.yml`.

You can change weather location in `weather-script.py`, find your location from [the Wunderground site](https://www.wunderground.com/weather/api/d/docs?d=data/forecast)



## Kindle side

Ensure the Kindle is jailbroken with USBNet.  Modify `weather-script.sh` to point to the correct image URL.

Copy the script files over to the Kindle:

    scp -r kindle/* root@192.168.1.72:/mnt/us/weather

SSH into the Kindle, and create a cron job for on boot by running

    /mnt/us/weather/utils/setupcrons.sh
    reboot

The reboot is necessary for the new cron task to take effect.


## Coding

The entry point is `weather-script.sh`, which first calls `weather-script.py`.  This Python script does the API call and parses the JSON. It also stores the JSON for 12 hours to avoid repeat calls. The condition, high and low values are extracted for three days and substituted in `weather-script-preprocess_temps.svg`.

The bash script then calls a few ImageMagick utilities; `convert` converts the SVG to a PNG, and `pngcrush` shrinks the image down.

Finally the script copies the output to a location visible over http in the Docker container, by default  http://localhost:9000/weather-script-output.png


## Original

This is a fork of a fork of a fork of a fork with several modifications for time over weather.

I've also had to ditch the MetOffice API which was becoming very unreliable. 

Base script from:
http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/
