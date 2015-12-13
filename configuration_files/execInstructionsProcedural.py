import RPi.GPIO as GPIO
import time

# Setup pins for spinning direction of the left and right motor (IN1 TO IN4)
leftIN1_motor_pin = 27
leftIN2_motor_pin = 22
rightIN1_motor_pin = 24
rightIN2_motor_pin = 25

# Setup the PWM pins for motor power (ENABLESA AND ENABLESB)
leftPWM1_motor_pin = 4
leftPWM2_motor_pin = 17
rightPWM1_motor_pin = 26
rightPWM2_motor_pin = 23

#GPIO number
GPIO.setmode(GPIO.BCM)

# Set the motor spinning pins as GPIO OUTPUT
GPIO.setup(leftIN1_motor_pin, GPIO.OUT)
GPIO.setup(leftIN2_motor_pin, GPIO.OUT)
GPIO.setup(rightIN1_motor_pin, GPIO.OUT)
GPIO.setup(rightIN2_motor_pin, GPIO.OUT)
# Set the motor PWM pins as GPIO OUTPUT
GPIO.setup(leftPWM1_motor_pin, GPIO.OUT)
GPIO.setup(leftPWM2_motor_pin, GPIO.OUT)
GPIO.setup(rightPWM1_motor_pin, GPIO.OUT)
GPIO.setup(rightPWM2_motor_pin, GPIO.OUT)
# Create PWM instance (channel, frequency)
motorPWM_left1 = GPIO.PWM(leftPWM1_motor_pin, 100)
motorPWM_left2 = GPIO.PWM(leftPWM2_motor_pin, 100)
motorPWM_right1 = GPIO.PWM(rightPWM1_motor_pin,100)
motorPWM_right2 = GPIO.PWM(rightPWM2_motor_pin,100)
# Turn on the engines at duty cycle equals to 0
motorPWM_left1.start(0)
motorPWM_left2.start(0)
motorPWM_right1.start(0)
motorPWM_right2.start(0)

def run(name, values):
    if name == "stop":
        stop(values.get('duration'))
    elif name == "move":
        move(values.get('duration'), values.get('power'), values.get('orientation'))
    elif name == "turn":
        turn(values.get('degree'), values.get('power'))
    elif name == "sensorDistance":
        print "sensorDistance"
    else:
        print "Instruction not mapped"

def move(duration, power, orientation):
    print "move"
    # Change duty cycle
    motorPWM_left1.ChangeDutyCycle(power)
    motorPWM_left2.ChangeDutyCycle(power)
    motorPWM_right1.ChangeDutyCycle(power)
    motorPWM_right2.ChangeDutyCycle(power)

    if orientation == 0:
        # Move forward
        GPIO.output(leftIN1_motor_pin, True)
        GPIO.output(leftIN2_motor_pin, False)
        GPIO.output(rightIN1_motor_pin, True)
        GPIO.output(rightIN2_motor_pin, False)

    elif orientation == 1:
        # Move backward
        GPIO.output(leftIN1_motor_pin, False)
        GPIO.output(leftIN2_motor_pin, True)
        GPIO.output(rightIN1_motor_pin, False)
        GPIO.output(rightIN2_motor_pin, True)
        # Sleep for 'duration' minutes

    # Sleep for 'duration' minutes
    time.sleep(duration)

def turn(degree, power):
    print "turn"
    # Make it turn
    motorPWM_left1.ChangeDutyCycle(power)
    motorPWM_left2.ChangeDutyCycle(power)
    motorPWM_right1.ChangeDutyCycle(power)
    motorPWM_right2.ChangeDutyCycle(power)

    if degree == 0:
        # Turn left
        GPIO.output(leftIN1_motor_pin, True)
        GPIO.output(leftIN2_motor_pin, False)
        GPIO.output(rightIN1_motor_pin, False)
        GPIO.output(rightIN2_motor_pin, True)

    elif degree == 1:
        # Move backward
        GPIO.output(leftIN1_motor_pin, False)
        GPIO.output(leftIN2_motor_pin, True)
        GPIO.output(rightIN1_motor_pin, True)
        GPIO.output(rightIN2_motor_pin, False)

    # Sleep for 'duration' minutes
    time.sleep(3)

def stop(duration):
    print "stop"
    motorPWM_left1.ChangeDutyCycle(0)
    motorPWM_left2.ChangeDutyCycle(0)
    motorPWM_right1.ChangeDutyCycle(0)
    motorPWM_right2.ChangeDutyCycle(0)
    # Disable movimentation for 'duration' seconds
    GPIO.output(leftIN1_motor_pin, False)
    GPIO.output(leftIN2_motor_pin, False)
    GPIO.output(rightIN1_motor_pin, False)
    GPIO.output(rightIN2_motor_pin, False)
    # Sleep for 'duration' seconds
    time.sleep(duration)

def cleanGPIO():
    print "GPIO cleanup"
    # Clean GPIO pins
    GPIO.cleanup()

def clearPWM():
    print "Clear PWM"
    # Change duty cycle to 0
    motorPWM_left1.ChangeDutyCycle(0)
    motorPWM_left2.ChangeDutyCycle(0)
    motorPWM_right1.ChangeDutyCycle(0)
    motorPWM_right2.ChangeDutyCycle(0)
    # Disable movimentation for 'duration' seconds
    GPIO.output(leftIN1_motor_pin, False)
    GPIO.output(leftIN2_motor_pin, False)
    GPIO.output(rightIN1_motor_pin, False)
    GPIO.output(rightIN2_motor_pin, False)
