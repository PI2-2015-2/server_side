import RPi.GPIO as GPIO
import time

class ExecInstructions():

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

    # Constructor of class
    def __init__(self):
        #GPIO number
        GPIO.setmode(GPIO.BCM)

        # Set the motor spinning pins as GPIO OUTPUT
        GPIO.setup(self.leftIN1_motor_pin, GPIO.OUT)
        GPIO.setup(self.leftIN2_motor_pin, GPIO.OUT)
        GPIO.setup(self.rightIN1_motor_pin, GPIO.OUT)
        GPIO.setup(self.rightIN2_motor_pin, GPIO.OUT)
        # Set the motor PWM pins as GPIO OUTPUT
        GPIO.setup(self.leftPWM1_motor_pin, GPIO.OUT)
        GPIO.setup(self.leftPWM2_motor_pin, GPIO.OUT)
        GPIO.setup(self.rightPWM1_motor_pin, GPIO.OUT)
        GPIO.setup(self.rightPWM2_motor_pin, GPIO.OUT)
        # Create PWM instance (channel, frequency)
        self.motorPWM_left1 = GPIO.PWM(self.leftPWM1_motor_pin, 50)
        self.motorPWM_left2 = GPIO.PWM(self.leftPWM2_motor_pin, 50)
        self.motorPWM_right1 = GPIO.PWM(self.rightPWM1_motor_pin,50)
        self.motorPWM_right2 = GPIO.PWM(self.rightPWM2_motor_pin,50)


    def run(self, name, values):
        if name == "stop":
            self.stop(values.get('duration'))
        elif name == "move":
            self.move(values.get('duration'), values.get('power'), values.get('orientation'))
        elif name == "turn":
            self.turn(values.get('degree'), values.get('power'))
        elif name == "sensorDistance":
            print "sensorDistance"
        else:
            print "Instrucao nao mapeada"

    def move(self, duration, power, orientation):
        print "move"
        # Make it move
        self.motorPWM_left1.start(0)
        self.motorPWM_left1.ChangeDutyCycle(power)
        self.motorPWM_left2.start(0)
        self.motorPWM_left2.ChangeDutyCycle(power)
        self.motorPWM_right1.start(0)
        self.motorPWM_right1.ChangeDutyCycle(power)
        self.motorPWM_right2.start(0)
        self.motorPWM_right2.ChangeDutyCycle(power)

        if orientation == 0:
            # Move forward
            GPIO.output(self.leftIN1_motor_pin, True)
            GPIO.output(self.leftIN2_motor_pin, False)
            GPIO.output(self.rightIN1_motor_pin, True)
            GPIO.output(self.rightIN2_motor_pin, False)

        elif orientation == 1:
            # Move backward
            GPIO.output(self.leftIN1_motor_pin, False)
            GPIO.output(self.leftIN2_motor_pin, True)
            GPIO.output(self.rightIN1_motor_pin, False)
            GPIO.output(self.rightIN2_motor_pin, True)

        # Sleep for 'duration' minutes
        time.sleep(duration)
        # Stop
        self.motorPWM_left1.stop()
        self.motorPWM_left2.stop()
        self.motorPWM_right1.stop()
        self.motorPWM_right2.stop()

    def turn(self, degree, power):
        print "turn"
        # Make it turn
        self.motorPWM_left1.start(0)
        self.motorPWM_left1.ChangeDutyCycle(power)
        self.motorPWM_left2.start(0)
        self.motorPWM_left2.ChangeDutyCycle(power)
        self.motorPWM_right1.start(0)
        self.motorPWM_right1.ChangeDutyCycle(power)
        self.motorPWM_right2.start(0)
        self.motorPWM_right2.ChangeDutyCycle(power)

        if degree == 0:
            # Turn left
            GPIO.output(self.leftIN1_motor_pin, True)
            GPIO.output(self.leftIN2_motor_pin, False)
            GPIO.output(self.rightIN1_motor_pin, False)
            GPIO.output(self.rightIN2_motor_pin, True)

        elif degree == 1:
            # Move backward
            GPIO.output(self.leftIN1_motor_pin, False)
            GPIO.output(self.leftIN2_motor_pin, True)
            GPIO.output(self.rightIN1_motor_pin, True)
            GPIO.output(self.rightIN2_motor_pin, False)

        # Sleep for 'duration' minutes
        time.sleep(2)
        # Stop
        self.motorPWM_left1.stop()
        self.motorPWM_left2.stop()
        self.motorPWM_right1.stop()
        self.motorPWM_right2.stop()

    def stop(self, duration):
        print "stop"
        # Stop
        self.motorPWM_left1.stop()
        self.motorPWM_left2.stop()
        self.motorPWM_right1.stop()
        self.motorPWM_right2.stop()
        # Disable movimentation for 'duration' seconds
        GPIO.output(self.leftIN1_motor_pin, False)
        GPIO.output(self.leftIN2_motor_pin, False)
        GPIO.output(self.rightIN1_motor_pin, False)
        GPIO.output(self.rightIN2_motor_pin, False)
        # Sleep for 'duration' seconds
        time.sleep(duration)

    def cleanGPIO(self):
        print "GPIO cleanup"
        GPIO.cleanup()
