
## Server side

In the server directory, build the image

    docker build -t kindleweather .

Create running container

    docker-compose up -d

Image should become available at http://servername/weather-script-output.png



## Kindle side

Copy the script files over

    scp -r kindle root@192.168.1.72:/mnt/us/weather




Base script from:
http://www.mpetroff.net/archives/2012/09/14/kindle-weather-display/

My changes:
* Added to Docker container
* Set "LATITUDE" and "LONGITUDE" envronment variables in docker,
  for example Durham NH is 43.1339 lat., -70.9264 lon.
  (will default to Durham NH if you don't specify your town!)
* Server presents image file for Kindle at http://<your IP>:3000/weather-script-output.png
