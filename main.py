import ASUS.GPIO as GPIO
import dht11
import time
import datetime

# config
DHT11_PIN = 5
LED_G_PIN = 8
LED_Y_PIN = 10
LED_R_PIN = 12
DETECT_INTERVAL = 5

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.cleanup()

GPIO.setup(LED_G_PIN, GPIO.OUT)
GPIO.setup(LED_Y_PIN, GPIO.OUT)
GPIO.setup(LED_R_PIN, GPIO.OUT)


def resetled():
  GPIO.output(LED_G_PIN, GPIO.LOW)
  GPIO.output(LED_Y_PIN, GPIO.LOW)
  GPIO.output(LED_R_PIN, GPIO.LOW)


resetled()

# read dht11 data
instance = dht11.DHT11(pin=DHT11_PIN)

while True:
  result = instance.read()
  if result.is_valid():
    try:
      t = result.temperature
      h = result.humidity

      print("%s,%dC,%d%%" % (str(datetime.datetime.now()),
                             t, h))

      if 40 <= h <= 60:
        # Good
        resetled()
        GPIO.output(LED_G_PIN, GPIO.HIGH)
      elif 60 < h <= 75 or 40 > h >= 35:
        # warning
        resetled()
        GPIO.output(LED_Y_PIN, GPIO.HIGH)
      else:
        # bad
        resetled()
        GPIO.output(LED_R_PIN, GPIO.HIGH)
    except:
      print('Failed')

  time.sleep(DETECT_INTERVAL)
