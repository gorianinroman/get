import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)

leds =[21,20,16,12,7,8,25,24]
aux = [22,23,27,18,15,14,3,2]
k = 1
for k in range(8) :
    GPIO.setup(leds[k], GPIO.OUT)
    GPIO.setup(aux[k], GPIO.IN)
    GPIO.input(aux[k], 1)


while True :
    for k in range(8) :
        GPIO.output(leds[k], GPIO.input(aux[k]))
    