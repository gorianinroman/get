import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

dac = [26,19,13,6,5,11,9,10]
i = 1
number = list(range(len(dac)))
number = [0,1,0,0,0,0,0,0]
for i in range(8) :
    GPIO.setup(dac[i], GPIO.OUT)
i = 1
for i in range(8) : 
    GPIO.output(dac[i], number[i])
time.sleep(10)
i=1
for i in range(8) :
    GPIO.output(dac[i], 0)
i = 1
for i in range(8) :
    GPIO.output(dac[i], 0)

GPIO.cleanup()

