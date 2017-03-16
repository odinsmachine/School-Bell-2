import time
import datetime
import pygame


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

print("Welcome to School Bell 2")
print("- This program will cause the bell to chime four times a day at the selected times.")
print("- Currently School Bell is configured to go off Monday(0), Tuesday(1), and Wednesday(2) of each week.")
print("- After the program has gone through all three days and giving four chimes a day it will hibernate for...")
print("- twelve hours at a time until it detects a school day again.")

def hibernate():
    global bellWeeks
    global bellPause
    global bellDate
    global bellTime
    while bellPause == True:
        print("> Hibernation",datetime.datetime.today(),": Active")
        time.sleep(120)
        bellWeeks = 0
        bellDate = True
        bellTime = True
        dateCheck()

def schoolBell():
    global bellTime
    global bellTolls
    global bellTick
    while bellTime == True:
        time.sleep(5)
        curr_time = int(time.strftime("%H%M"))
        currentTime = curr_time
        print(">",currentTime,".",bellTick)
        bellTick = bellTick + 5
        if bellTolls < 4:               #: If program is started after one of the times has...
            if curr_time == 1511:       #: passed the counter will fail to end the loop.
                if bellTime == True:
                    print("> Bell chime!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("PuppetsDream.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime: ",bellTime)
                    bellTick = 5
                    
            elif curr_time == 1513:
                if bellTime == True:
                    print("> Bell chime!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("PuppetsDream.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime: ",bellTime)
                    bellTick = 5
            
            elif curr_time == 1515:
                if bellTime == True:
                    print("> Bell chime!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("PuppetsDream.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime: ",bellTime)
                    bellTick = 5
                    
            elif curr_time == 1517:
                if bellTime == True:
                    print("> Bell chime!")
                    pygame.mixer.init()
                    pygame.mixer.music.load("PuppetsDream.mp3")
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy() == True:
                        continue
                    bellTime = False
                    bellTolls = bellTolls + 1
                    time.sleep(60)
                    bellTime = True
                    print("> BellTime: ",bellTime)
                    bellTick = 5
        else:
            print(">",currentDate," School Day ending.")
            bellTime = False
            print("> BellTime: ",bellTime)
            dateCheck()
        
def dateCheck():
    global bellDate
    global currentTime
    global currentDate
    global bellTime
    global bellTolls
    global bellWeeks
    global bellPause
    global pid      
    while bellDate == True:
        time.sleep(5)
        datetime.datetime.today()
        currentDate = datetime.datetime.today().weekday()
        if bellWeeks < 3:
            if currentDate == 0:    #: < ---- Python displays the days as numbers with Monday being zero. The days of the week...       
                print(">",currentDate, " Monday: school day starting!") #: go from 0 - 7.
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell()
            elif currentDate == 1:
                print(">",currentDate, " Tuesday: school day starting!")
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell()
            elif currentDate == 4:
                print(">",currentDate, " Wednesday: school day starting!")
                bellTicks = 0
                bellTime = True
                bellWeeks = bellWeeks + 1
                schoolBell()
            else:
                print("> Day:",currentDate, "Not a school day:",pid)
                pid = pid + 1
        else:
            print("> This week has now completed, School Bell will now hibernate for 12 hours before checking the time again.")
            bellDate = False
            bellPause = True
            hibernate()
dateCheck()
