import paho.mqtt.client as mqtt

def connectAndSubscribe(client, userdata, flags, rc):
    mqttClient.subscribe("IOSTopic")

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
        import sensorController
        sensorController.setTrigger2()
    elif msg == "ActivateSensor":
        import sensorController
        sensorController.detect()
    elif msg == "CalcAverageLEDOn":
        import AutomationData
        AutomationData.autoMenu(1, 1)
    elif msg == "CalcAverageLEDOff":
        import AutomationData
        AutomationData.autoMenu(1, 2)
    elif msg == "CalcAverageLock":
        import AutomationData
        AutomationData.autoMenu(1, 3)
    elif msg == "CalcAverageLEDUnlock":
        import AutomationData
        AutomationData.autoMenu(1, 4)
        
    
    

mqttClient = mqtt.Client("IOSApp")
mqttClient.on_connect = connectAndSubscribe
mqttClient.connect("ServerAdress", "PortNumber")
mqttClient.loop_forever()
