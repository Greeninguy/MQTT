
import RPi.GPIO as GPIO
import time

height = 0

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
#set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18

def sensorSetup():
    #set GPIO direction (IN / OUT)
    GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
    GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    sensorSetup()
    
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
 
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
 
    StartTime = time.time()
    StopTime = time.time()
 
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
 
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
 
    return distance
    
#Manually set trigger distance for sensor
def setTrigger():
	print ("Enter Distance (cm) \n")
	trigger = input()
	proper = trigger.isdigit()
	while proper == false:
		print ("Please Enter a Number \n")
		trigger = input()
		proper = trigger.isdigit()
		print ("Height Threshold is now " + trigger)
	return trigger
    
#Use the sensor to set trigger distance
def setTrigger2():
    
    import RPi.GPIO as GPIO
    import time

    height = 0

    #GPIO Mode (BOARD / BCM)
    GPIO.setmode(GPIO.BOARD)
 
    #set GPIO Pins
    GPIO_TRIGGER = 12
    GPIO_ECHO = 18
    
    print ("Adjusting Trigger Distance \n")
    i = 4
    dist = 0
    while i > 1:
	dist += distance()
	i = i - 1
	time.sleep(1)
    trigger = dist / 4
    print ("Height Threshold is now " + trigger)
    f = open("HeightTrigger.txt", 'w')
    f.write(str(trigger))
    f.close()
    
def distanceTest():
    return 35
    
def sensorMenu():
    while True:
        print("Which Operation? \n"
              "Set Height (Manual Input): I \n"
              "Set Height (Sensor Input): S \n"
              "Activate Sensor: A \n"
              "Exit: E \n")
        answer = input()
        if answer == "i" or answer == "I":
            height = setTrigger()
        elif answer == "s" or answer == "S":
            height = setTrigger2()
        elif answer == "a" or answer == "A":
            detect(height)
        elif answer == "e" or answer == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input")

def detect():
    f = open("HeightTrigger.txt", 'r')
    height = f.read()
    f.close()
    height = int(height)
    try:
        while True:
            thresh = height
            dist = distance()
            if dist < thresh + 5:
                print ("Height Threshold Detected: Unlocking Gate")
                import LockController
                LockController.lockAfterUnlock()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(3)

    #Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        exit()
