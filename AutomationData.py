def autoMenu(inp1, inp2):
    while True:
        print("Which Operation? \n"
              "Calc Avgerage: A \n"
              "Set Average: S \n"
              "Clear File: C \n"
              "Exit: E \n")
        answer = inp
        if answer == 1:
            while True:
                print("Which Operation? \n"
                      "Turn LED On: O \n"
                      "Turn LED Off: F \n"
                      "Lock Gate: L \n"
                      "Unlock Gate: U \n"
                      "Exit/Go Back: E \n")
                answer = inp2
                if answer == 1:
                    return calcLEDOn()
                elif answer == 2:
                    return calcLEDOff()
                elif answer == 3:
                    return calcLock()
                elif answer == 4:
                    return calcUnlock()
                else:
                    print("Invalid input")
        elif answer == 's' or answer == 'S':
            print("Which Operation? \n"
                  "Turn LED On: O \n"
                  "Turn LED Off: F \n"
                  "Lock Gate: L \n"
                  "Unlock Gate: U \n")
            answer = input()
            if answer == 'o' or answer == 'O':
                file = "LEDOnAuto.txt"
            elif answer == 'f' or answer == 'F':
                file = "LEDOffAuto.txt"
            elif answer == 'l' or answer == 'L':
                file = "LockAuto.txt"
            elif answer == 'u' or answer == 'U':
                file = "UnlockAuto.txt"
            f = open(file, 'w')
            print("What Day? (0-6) \n")
            answer = input()
            f.write(str(answer))
            f.write('\n')
            print("Which Hour? (0-23) \n")
            answer = input()
            f.write(str(answer))
            f.write('\n')
            print("Which Minute? (0-59) \n")
            answer = input()
            f.write(str(answer))
            f.write('\n')
            f.close()
        elif answer == 2:
            print("Which File?")
            answer = inp2
            clearFile(answer)
        elif answer == "e" or answer == "E":
            print("Exiting program...")
            exit()
        else:
            print("Invalid input")

def calcAvg(day, hour, minute):
    lists = [day, hour, minute]
    averages = []
    for i in lists:
        x = 0
        avg = 0
        for j in i:
            avg = avg + j
            x = x + 1
        avg = avg / x
    averages.append(int(avg))
    print("Averages are " + averages)
    return averages

def readFile(file):
    f = open(file, 'r')
    lis = f.read().splitlines()
    f.close()
    lis = list(map(int, lis))
    return lis

def clearFile(file):
    try:
        open(file, 'r')
        f = open(file, 'w')
        f.write('')
        print("File " + file + " has been cleared.")
        f.close()
    except IOError:
        print("Error: File not found")
    
def calcLEDOn():
    day = readFile("ledonday.txt")
    hour = readFile("ledonhour.txt")
    minute = readFile("ledonminute.txt")
    return calcAvg(day, hour, minute)
    
def calcLEDOff():
    day = readFile("ledoffday.txt")
    hour = readFile("ledoffhour.txt")
    minute = readFile("ledoffminute.txt")
    return calcAvg(day, hour, minute)

def calcLock():
    day = readFile("lockday.txt")
    hour = readFile("lockhour.txt")
    minute = readFile("lockminute.txt")
    return calcAvg(day, hour, minute)

def calcUnlock():
    day = readFile("unlockday.txt")
    hour = readFile("unlockhour.txt")
    minute = readFile("unlockminute.txt")
    return calcAvg(day, hour, minute)

def setAuto(averages, file):
    if len(averages) == 3:
        f.open(file, 'w')
        f.write(str(averages[0]))
        f.write('\n')
        f.write(str(averages[1]))
        f.write('\n')
        f.write(str(averages[2]))
        f.write('\n')
        f.close()
    else:
        print("Error: This function does not have averages.)
