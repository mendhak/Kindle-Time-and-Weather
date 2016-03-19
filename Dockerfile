FROM phusion/baseimage:0.9.16

# Use baseimage-docker's init system
CMD ["/sbin/my_init"]

#Install dependencies
RUN apt-get update
RUN apt-get install -y python cron lighttpd librsvg2-bin pngcrush imagemagick rsyslog

#Add files
RUN mkdir /www
RUN mkdir /www/root
ADD ./server /www

RUN cron
#Set up cron job for updating weather forecast
RUN crontab -l | { cat; echo "* * * * * cd /www ; /www/weather-script.sh"; } | crontab -

#Run script once initially
#RUN /www/weather-script.sh

#Run web server
CMD /usr/sbin/lighttpd -f /www/lighttpd.conf && cron -f
