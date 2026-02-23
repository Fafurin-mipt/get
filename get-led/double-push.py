import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16]

GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

up = 9
down = 10
GPIO.setup(up, GPIO.IN)
GPIO.setup(down, GPIO.IN)

num = 0
MAX_NUM = 255

sleep_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:

    if GPIO.input(up) and GPIO.input(down):
        num = MAX_NUM
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)
        continue


    elif GPIO.input(up):
        num += 1
        if num > MAX_NUM:
            num = MAX_NUM
        print(num, dec2bin(num))
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)

    elif GPIO.input(down):
        num -= 1
        if num < 0:
            num = 0
        print(num, dec2bin(num)) 
        GPIO.output(leds, dec2bin(num))
        time.sleep(sleep_time)