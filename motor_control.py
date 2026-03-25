import RPi.GPIO as GPIO

# Motor Pins
IN1 = 17
IN2 = 27
IN3 = 22
IN4 = 23
ENA = 12
ENB = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup([IN1, IN2, IN3, IN4], GPIO.OUT)
GPIO.setup([ENA, ENB], GPIO.OUT)

# PWM setup
pwm_left = GPIO.PWM(ENA, 100)
pwm_right = GPIO.PWM(ENB, 100)

pwm_left.start(0)
pwm_right.start(0)

speed = 60  # default speed


def set_speed(value):
    global speed
    speed = value


def move_forward():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)


def move_backward():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)


def turn_left():
    GPIO.output(IN1, False)
    GPIO.output(IN2, True)
    GPIO.output(IN3, True)
    GPIO.output(IN4, False)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)


def turn_right():
    GPIO.output(IN1, True)
    GPIO.output(IN2, False)
    GPIO.output(IN3, False)
    GPIO.output(IN4, True)
    pwm_left.ChangeDutyCycle(speed)
    pwm_right.ChangeDutyCycle(speed)


def stop():
    GPIO.output([IN1, IN2, IN3, IN4], False)
    pwm_left.ChangeDutyCycle(0)
    pwm_right.ChangeDutyCycle(0)