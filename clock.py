#!/usr/bin/env python3

import os, time, pygame

# Initialize PyGame...
os.putenv('SDL_VIDEODRIVER', 'fbcon')  # works for 320x240 Adafruit PiTFT
os.putenv('SDL_FBDEV', '/dev/fb1')     # which is treated as a framebuffer
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.font.init()

# Miscellaneous setup for clock...
font_hhmm = pygame.font.Font(None, 180)
font_ss = pygame.font.Font(None,  100)
font_ss2 = pygame.font.Font(None,  58)
black = (0, 0, 0)      # RGB tuples
green = (0, 255, 0)
white = (255, 255, 255)
last_second_shown = 0  # seconds past the epoc (midnight 1970-01-01 UTC)

# Loop to display updated clock each second...
now = time.time()
last_minute = int(now)


#READ INFO FROM FILE CREATED BY CRON JOB
file = open("/home/pi/picryptoclock/btcprice.txt","r") 
linedata = file.readline()
linedata = linedata.split("|")
price = linedata[0]
mktcap = linedata[1]
file.close()
ss = "BTC: $" + str(price)
mc = "Total Market Cap: $" + str(mktcap) + "b"

while True:
    now = time.time()
    current_second = int(now)
    
    if current_second != last_second_shown:  # if a new/different second...
        last_second_shown = current_second
        screen.fill(black)  # erase everything        
        
        if (current_second >= last_minute + 60):
            last_minute = current_second
            file = open("/home/pi/picryptoclock/btcprice.txt","r") 
            linedata = file.readline()
            linedata = linedata.split("|")
            price = linedata[0]
            mktcap = linedata[1]
            file.close()
            ss = "BTC: $" + str(price)
            mc = "Total Market Cap: $" + str(mktcap) + "b"

        #IF YOU DON'T WANT YOUR SCREEN FLIPPED THEN YOU WILL NEED TO
        #REMOVE pygame.transform.rotate(ss_surface, 180) AND JUST PASS IN ss_surface INSTEAD
        #YOU WILL ALSO NEED TO PLAY AROUND WITH xy and xy2

        ss_surface = font_ss.render(ss, True, white, black)
        #xy2 = xy[0] + hhmm_surface.get_width(), xy[1] + 50  # follows HH:MM
        xy3 = (40, 100)  # where to draw
        screen.blit(pygame.transform.rotate(ss_surface, 180), xy3)            
        
        ss_surface = font_ss2.render(mc, True, white, black)
        #xy2 = xy[0] + hhmm_surface.get_width(), xy[1] + 50  # follows HH:MM
        xy2 = (10, 30)  # where to draw
        screen.blit(pygame.transform.rotate(ss_surface, 180), xy2)          
        
        tm = time.localtime(now)

        # draw HH:MM on screen
        hhmm = '{:02}:{:02}:{:02}'.format(tm.tm_hour, tm.tm_min, tm.tm_sec)
        hhmm_surface = font_hhmm.render(hhmm, True, white, black)
        xy = (5, 190)  # where to draw
        
        screen.blit(pygame.transform.rotate(hhmm_surface, 180), xy)
        #screen.blit(hhmm_surface, xy)

        # draw :SS on screen (following HH:MM, slightly smaller)
        
        #screen.blit(ss_surface, xy2)
        pygame.display.update()  # and have PyGame display the updated screen

    pygame.time.wait(200)  # Wait 1/5th of a second before checking again
