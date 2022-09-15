import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [21,20,16,12,7,8,25,24]
k = 1
for k in range(8) :
    GPIO.setup(leds[k], GPIO.OUT)
k = 1
i = 1
j = 1
for i in range(3) :
    for j in range(8) :
        GPIO.output(leds[j], 1)
        time.sleep(0.2)
        GPIO.output(leds[j], 0)
for k in range(8) :
    GPIO.output(leds[k], 0)

GPIO.cleanup()