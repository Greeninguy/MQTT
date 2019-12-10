import paho.mqtt.client as mqtt

def connectAndSubscribe(client, userdata, flags, rc):
    mqttClient.subscribe("iosToRpi")

def processMessage(client, userdata, message):
    topic = str(message.topic)
    msg = str(message.payload.decode("utf-8"))

    #These strings are what I have setup to activate the controller scripts
    if msg == "LEDOn":
        import LEDController
        LEDController.turnOn()
        print("Turned LED On.")
    elif msg == "LEDOff":
        import LEDController
        LEDController.turnOff()
        print("Turned LED Off.")
    elif msg == "Lock":
        import LockController
        LockController.lock()
        print("Locked Gate.")
    elif msg == "Unlock":
        import LockController
        LockController.unlock()
        print("Unlocked Gate")
    elif msg == "SetSensorHeight":
        print("Setting Sensor Height Threshold")
        import sensorController
        height = msg[17:]
        sensorController.setTrigger(height)
    elif msg == "SetSensorHeight2":
        print("Setting Sensor Height Threshold")
        import sensorController
        sensorController.setTrigger2()
    elif msg == "ActivateSensor":
        print("Activating Sensor")
        import sensorController
        sensorController.detect()
    elif msg == "CalcAverageLEDOn":
        import AutomationData
        averages = AutomationData.calcLEDOn()
        AutomationData.setAuto(averages, "LEDOnAuto.txt")
    elif msg == "CalcAverageLEDOff":
        import AutomationData
        averages = AutomationData.calcLEDOff()
        AutomationData.setAuto(averages, "LEDOffAuto.txt")
    elif msg == "CalcAverageLock":
        import AutomationData
        averages = AutomationData.calcLock()
        AutomationData.setAuto(averages, "LockAuto.txt")
    elif msg == "CalcAverageLEDUnlock":
        import AutomationData
        averages = AutomationData.calcUnlock()
        AutomationData.setAuto(averages, "UnlockAuto.txt")
    elif msg == "ClearLEDOnAuto":
        import AutomationData
        AutomationData.clearFile("LEDOnAuto.txt")
    elif msg == "ClearLEDOnData":
        import AutomationData
        AutomationData.clearFile("ledonday.txt")
        AutomationData.clearFile("ledonhour.txt")
        AutomationData.clearFile("ledonminute.txt")
    elif msg == "ClearLEDOffAuto":
        import AutomationData
        AutomationData.clearFile("LEDOffAuto.txt")
    elif msg == "ClearLEDOffData":
        import AutomationData
        AutomationData.clearFile("ledoffday.txt")
        AutomationData.clearFile("ledoffhour.txt")
        AutomationData.clearFile("ledoffminute.txt")
    elif msg == "ClearLockAuto":
        import AutomationData
        AutomationData.clearFile("LockAuto.txt")
    elif msg == "ClearLockData":
        import AutomationData
        AutomationData.clearFile("lockday.txt")
        AutomationData.clearFile("lockhour.txt")
        AutomationData.clearFile("lockminute.txt")
    elif msg == "ClearUnlockAuto":
        import AutomationData
        AutomationData.clearFile("UnlockAuto.txt")
    elif msg == "ClearUnlockData":
        import AutomationData
        AutomationData.clearFile("unlockday.txt")
        AutomationData.clearFile("unlockhour.txt")
        AutomationData.clearFile("unlockminute.txt")
    elif msg == "TurnOnAuto":
        import Automation
    elif msg == "RequestAutoLEDOn.txt":
        f = open("LEDOnAuto.txt", 'r')
        auto = f.read()
        #send auto via MQTT
    elif msg == "RequestAutoLEDOff.txt":
        f = open("LEDOffAuto.txt", 'r')
        auto = f.read()
        #send auto via MQTT
    elif msg == "RequestAutoLock.txt":
        f = open("LockAuto.txt", 'r')
        auto = f.read()
        #send auto via MQTT
    elif msg == "RequestAutoUnlock.txt":
        f = open("UnlockAuto.txt", 'r')
        auto = f.read()
        #send auto via MQTT
        
        
    
    

mqttClient = mqtt.Client("RPI")
mqttClient.on_connect = connectAndSubscribe
mqttClient.connect("127.8.8.1")
mqttClient.loop_forever()
