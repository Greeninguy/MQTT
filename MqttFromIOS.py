import paho.mqtt.client as mqtt

def connectAndSubscribe(client, userdata, flags, rc):
    mqttClient.subscribe("iosToRpi")

def processMessage(client, userdata, message):
    topic = str(message.topic)
    msg = str(message.payload.decode("utf-8"))
    print("Recieved Message: " + msg)

    #These strings are what I have setup to activate the controller scripts
    if msg == "LED":
        import LEDController
        LEDController.operateLED()
    elif msg == "Lock":
        import LockController
        LockController.operateLock()
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
        import AutomationData
        averages = AutomationData.calcUnlock()
        stringed = ""
        for x in averages:
            stringed = stringed + x
        mqttClient.publish("rpiToIos", stringed)
    elif msg == "RequestAutoUnlock.txt":
        f = open("UnlockAuto.txt", 'r')
        auto = f.read()
        #send auto via MQTT
    elif msg == "Yes":
        import AutomationData
        averages = AutomationData.calcUnlock()
        AutomationData.setAuto(averages, "UnlockAuto.txt")
        print("Set automation for Lock.")
        
    
mqttClient = mqtt.Client("RPI")
mqttClient.on_connect = connectAndSubscribe
mqttClient.connect("localhost")
mqttClient.loop_forever()
