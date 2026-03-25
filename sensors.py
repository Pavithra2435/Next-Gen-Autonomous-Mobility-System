import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# IR sensors
IR_LEFT = 5
IR_RIGHT = 6

# Ultrasonic sensor
TRIG = 18
ECHO = 24

GPIO.setup(IR_LEFT, GPIO.IN)
GPIO.setup(IR_RIGHT, GPIO.IN)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)


def get_lane_status():
    return GPIO.input(IR_LEFT), GPIO.input(IR_RIGHT)


def get_distance():
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    start = time.time()
    end = time.time()

    while GPIO.input(ECHO) == 0:
        start = time.time()

    while GPIO.input(ECHO) == 1:
        end = time.time()

    duration = end - start
    distance = (duration * 34300) / 2

    return distance