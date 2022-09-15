import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
leds = [21,20,16,12,7,8,25,24]
for k in range(8) :
    GPIO.setup(leds[k], GPIO.OUT)
for k in range(8) :
    GPIO.output(leds[k], 0)
GPIO.cleanup()