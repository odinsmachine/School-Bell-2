import time
import datetime
#import pygame

bellTolls = 0
currentTime = 0
currentDate = ""
bellTime = False
bellDate = True
bellChime = False
bellPause = False
bellTick = 5
bellWeeks = 2
pid = 0
#: user set values
bellValue01 = 0
bellValue02 = 0
bellValue03 = 0
bellValue04 = 0

print("Welcome to School Bell 2\n\n" \
    "- This program will cause the bell to chime four times a day at the selected times.\n" \
    "- Currently School Bell is configured to go off Monday(0), Tuesday(1), and Wednesday(2) of each week.\n" \
    "- After the program has gone through all three days and giving four chimes a day it will hibernate for...\n" \
    "- twelve hours at a time until it detects a school day again.\n")

print("Please select the four times you would like for you school bell to be activated." \
    "\nNote that you have to use a 24 hour time format with no separators" \
    "for example '1530' would be a vaild input.")
curr_time = int(time.strftime("%H%M"))
currentTime = curr_time
print("The time is currenlty,",curr_time)

bellValue01 = input("First time: ").lower()
if bellValue01 == "pass":
    bellValue01 = 0
    print("First time skipped.")
else:
    bellValue01 = int(bellValue01)
    print(bellValue01)
bellValue02 = input("Second time: ").lower()
if bellValue02 == "pass":
    bellValue02 = 0
    print("Second time skipped")
else:
    bellValue02 = int(bellValue02)
    print(bellValue02)
bellValue03 = input("Third time: ").lower()
if bellValue03 == "pass":
    bellValue03 = 0
    print("Third time skipped.")
else:
    bellValue03 = int(bellValue03)
    print(bellValue03)
bellValue04 = input("Fourth time: ").lower()
if bellValue04 == "pass":
    bellValue04 = 0
    print("Fourth time skipped")
else:
    bellValue04 = int(bellValue04)
    print(bellValue04)
def schoolBell(bellTime,bellTolls,bellTick,bellValue01,bellValue02,bellValue03,bellValue04):
    while bellTime == True:
        time.sleep(5)
        datetime.datetime.today()
        currentDate = datetime.datetime.today().weekday()
        curr_time = int(time.strftime("%H%M"))
        currentTime = curr_time
        print("> Day:",currentDate,"Time:",currentTime,"PID:",bellTick)
        bellTick = bellTick + 5
        if bellTolls < 4:   #: If program is started after one of the times has passed the counter will fail to end the loop.
            #: BELL TOLL - ONE
            if curr_time == bellValue01:
                if bellTime == True:
                    print("> Bell chime!")
                    #pygame.mixer.init()
                    #pygame.mixer.music.load("PuppetsDream.mp3")
                    #pygame.mixer.music.play()
                    #while pygame.mixer.music.get_busy() == True:
                    #    continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime:",bellTime)
                    bellTick = 5
            #: BELL TOLL - TWO
            elif curr_time == bellValue02:
                if bellTime == True:
                    print("> Bell chime!")
                    #pygame.mixer.init()
                    #pygame.mixer.music.load("PuppetsDream.mp3")
                    #pygame.mixer.music.play()
                    #while pygame.mixer.music.get_busy() == True:
                    #    continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime:",bellTime)
                    bellTick = 5
            #: BELL TOLL - THREE
            elif curr_time == bellValue03:
                if bellTime == True:
                    print("> Bell chime!")
                    #pygame.mixer.init()
                    #pygame.mixer.music.load("PuppetsDream.mp3")
                    #pygame.mixer.music.play()
                    #while pygame.mixer.music.get_busy() == True:
                    #    continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime:",bellTime)
                    bellTick = 5
            #: BELL TOLL - FOUR
            elif curr_time == bellValue04:
                if bellTime == True:
                    print("> Bell chime!")
                    #pygame.mixer.init()
                    #pygame.mixer.music.load("PuppetsDream.mp3")
                    #pygame.mixer.music.play()
                    #while pygame.mixer.music.get_busy() == True:
                    #    continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime:",bellTime)
                    bellTick = 5
        else:
            print(">",currentDate," School Day ending.")
            bellTime = False
            print("> BellTime:",bellTime)
            dateCheck(currentTime,currentDate,bellDate,bellTime,bellTolls,bellWeeks,bellPause)
        
def dateCheck(bellTolls,currentTime,currentDate,bellTime,bellDate,bellChime,bellPause,bellTick,bellWeeks,pid):    
    while bellDate == True:
        time.sleep(5)
        datetime.datetime.today()
        currentDate = datetime.datetime.today().weekday()
        if bellWeeks < 3:
            if currentDate == 0:    #: < ---- Python displays the days as numbers with Monday being zero. The days of the week...       
                print(">",currentDate, "Monday: school day starting!") #: go from 0 - 7.
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell(bellTime,bellTolls,bellTick,bellValue01,bellValue02,bellValue03,bellValue04)
            elif currentDate == 1:
                print(">",currentDate, "Tuesday: school day starting!")
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell(bellTime,bellTolls,bellTick,bellValue01,bellValue02,bellValue03,bellValue04)
            elif currentDate == 2:
                print(">",currentDate, "Wednesday: school day starting!")
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell(bellTime,bellTolls,bellTick,bellValue01,bellValue02,bellValue03,bellValue04)
            else:
                print("> Day:",currentDate, "Not a school day:",pid)
                pid = pid + 1
        else:
            print("> This week has now completed, School Bell will now hibernate for 12 hours before checking the time again.")
            bellDate = False
            bellPause = True
            time.sleep(30)
dateCheck(bellTolls,currentTime,currentDate,bellTime,bellDate,bellChime,bellPause,bellTick,bellWeeks,pid)


