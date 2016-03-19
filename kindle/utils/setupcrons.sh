#!/bin/sh

mntroot rw
echo "Adding line to crontab"
grep -q -F '* * * * * /bin/bash /mnt/us/weather/init-weather.sh' /etc/crontab/root || echo '* * * * * /bin/bash /mnt/us/weather/init-weather.sh' >> /etc/crontab/root
echo "Please reboot!!"
#Don't automatically reboot, I got caught in a boot loop and only barely managed to escape...
