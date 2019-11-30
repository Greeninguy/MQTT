def setup():   
    import RPi.GPIO as GPIO
    import datetime
    from datetime import datetime

    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)

    ledPin = 31

    GPIO.setup(ledPin, GPIO.OUT)

def turnOn():
    import RPi.GPIO as GPIO
    import datetime
    from datetime import datetime
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    ledPin = 31
    GPIO.setup(ledPin, GPIO.OUT)
    
    print("Turning on light.")
    d = datetime.today()
    t = d.timetuple()
    f = open("ledonday.txt", 'a')
    f.write(str(d.weekday()))
    f.write('\n')
    f.close()
    f = open("ledonhour.txt", 'a')
    f.write(str(t[3]))
    f.write('\n')
    f.close()
    f = open("ledonminute.txt", 'a')
    f.wright(str(t[4]))
    f.write('\n')
    f.close()
    GPIO.output(ledPin, GPIO.HIGH)

def turnOff():
    import RPi.GPIO as GPIO
    import datetime
    from datetime import datetime
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    ledPin = 31
    GPIO.setup(ledPin, GPIO.OUT)
    
    print("Turning off light.")
    d = datetime.today()
    t = d.timetuple()
    f = open("ledoffday.txt", 'a')
    f.write(str(d.weekday()))
    f.write('\n')
    f.close()
    f = open("ledoffhour.txt", 'a')
    f.write(str(t[3]))
    f.write('\n')
    f.close()
    f = open("ledoffminute.txt", 'a')
    f.wright(str(t[4]))
    f.write('\n')
    f.close()
    GPIO.output(ledPin, GPIO.LOW)
    
def LEDMenu():
    while True:
        print("Which Operation? \n"
            "Turn On: T \n"
            "Turn Off: R \n"
            "Exit: E \n")
        answer = input()
        if answer == "t" or answer == "T":
            turnOn()
        elif answer == "r" or answer == "R":
            turnOff()
        elif answer == "e" or answer == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input")
