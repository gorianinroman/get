import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(26, GPIO.IN)
GPIO.output(17, GPIO.input(26))

while True :
    GPIO.output(17, GPIO.input(26))