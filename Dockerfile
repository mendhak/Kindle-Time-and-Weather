FROM phusion/baseimage:0.9.16

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#Install dependencies
RUN apt-get update
RUN apt-get install python cron lighttpd librsvg2-bin pngcrush

#Set up cron job for updating weather forecast
RUN crontab -l | { cat; echo "25,55 * * * * /www/weather-script.sh"; } | crontab -


#Add files
RUN mkdir /www
RUN mkdir /www/root
ADD ./server /www

#Run web server
CMD[lighttpd -D -f /www/lighttpd.conf]