import ASUS.GPIO as GPIO
import lib/dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=5)

deviceId = 'wzaHMXe3G0NweRFW'

while True:
    result = instance.read()
    if result.is_valid():
        print("Last valid input: " + str(datetime.datetime.now()))
        print("Temperature: %d C" % result.temperature)
        print("Humidity: %d %%" % result.humidity)

        r = requests.post("http://localhost/api/device/insertData", json={
            "deviceId": deviceId,
            "data":{
                "humidity": result.humidity,
                "temparature": result.temperature
            }
        })

    time.sleep(1)
