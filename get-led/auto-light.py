import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
GPIO.setup(led, GPIO.OUT)

photo = 6
GPIO.setup(photo, GPIO.IN)

state = 0

while True:
    GPIO.output(led, not GPIO.input(photo))
    time.sleep(0.1)
    