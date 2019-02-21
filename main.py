import ASUS.GPIO as GPIO
import dht11
import time
import datetime
import requests

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

# read data using pin 14
instance = dht11.DHT11(pin=5)

deviceId = 'DTQj4ROiclK7aT4K'

while True:
  result = instance.read()
  if result.is_valid():
    print("%s,%dC,%d%%" % (str(datetime.datetime.now()),
                           result.temperature, result.humidity))

    try:
      r = requests.post("https://wettycat.duckdns.org/api/device/insertData", json={
          "deviceId": deviceId,
          "data": {
              "humidity": result.humidity,
              "temperature": result.temperature
          }
      })
    except:
      print('Upload Failed')

  time.sleep(2)
