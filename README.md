# Raspberry Pi Crypto Clock (3.5" TFT)

 - clock.py - The clock
 - getprice.py - Program to get API data (run by cron job)

### Display Data 
hh:mm:ss
BTC: $9,999
Total Market Cap: $999b

## Setup

Clone this repo:

```sh
$ git clone https://github.com/pigd0g/picryptoclock
```

### Cron Jobs
```sh
$ crontab -e
```
Add the following lines:
```sh
#EVERY 10 MINS & AT REBOOT
*/10 * * * * /usr/bin/python /home/pi/picryptoclock/getprice.py
@reboot /usr/bin/python /home/pi/picryptoclock/getprice.py
```

### Run at Startup

Find the folder /home/pi/.config/lxsession/LXDE-pi

In this folder put a file named autostart containing one line specifying the full path of the file to be executed:

```sh
python /home/pi/picryptoclock/clock.py
```

Make the autostart file executable by chmod +x autostart

### LCD Setup

https://github.com/goodtft/LCD-show

### Disable Screensaver (Blank Screen)

https://www.raspberrypi.org/forums/viewtopic.php?t=57552


### Credits
Original Clock Source - https://www.raspberrypi.org/forums/viewtopic.php?t=166188
Post by this member - https://www.raspberrypi.org/forums/memberlist.php?mode=viewprofile&u=101632

