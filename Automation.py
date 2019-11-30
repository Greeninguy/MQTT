import LEDController
import LockController
import os
import datetime
from datetime import datetime
import time

def automate():
    try:
        while True:
            theTime = timeCheck()
            match = readAuto("LEDOnAuto.txt", theTime)
            if match:
                LEDController.turnOn()
            match = readAuto("LEDOffAuto.txt", theTime)
            if match:
                LEDController.turnOff()
            match = readAuto("LockAuto.txt", theTime)
            if match:
                LockController.lock()
            match = readAuto("UnlockAuto.txt", theTime)
            if match:
                LockController.unlock()
            time.sleep(60)
    except KeyboardInterrupt:
        exit()

def readAuto(file, time):
    if os.stat(file).st_size == 0:
        return false
    f = open(file, 'r')
    lis = f.read().splitlines()
    f.close()
    lis = list(map(int,lis))
    if lis[0] == time[0] and lis[1] == time[1] and lis[2] == time[2]:
        return True
    else:
        return False

def timeCheck():
    d = datetime.today()
    t = d.timetuple()
    time = []
    time.append(d.weekday())
    time.append(t[3])
    time.append(t[4])
    return time

automate()
