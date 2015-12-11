import RPi.GPIO as GPIO
import time

#GPIO number
GPIO.setmode(GPIO.BCM)

# Disable warning from GPIO
GPIO.setwarnings(False)

# Setup Power Frequency and Duty Cycle
PWM_FREQ_MAX = 100
DUTY_CYCLE_MAX = 100

# Setup pins for spinning direction of the left motor
leftmotor_in1_pin = 27
leftmotor_in2_pin = 22
GPIO.setup(leftmotor_in1_pin, GPIO.OUT)
GPIO.setup(leftmotor_in2_pin, GPIO.OUT)

# Setup pins for spinning direction of the right motor
rightmotor_in1_pin = 24
rightmotor_in2_pin = 25
GPIO.setup(rightmotor_in1_pin, GPIO.OUT)
GPIO.setup(rightmotor_in2_pin, GPIO.OUT)

# Setup pins for left motor power
leftpwd_in1_pin = 4
leftpwm_in2_pin = 17
GPIO.setup(leftpwd_in1_pin, GPIO.OUT)
GPIO.setup(leftpwm_in2_pin, GPIO.OUT)
motorpwm1 = GPIO.PWM(leftpwd_in1_pin, 100)
motorpwm3 = GPIO.PWM(leftpwm_in2_pin, 100)
motorpwm1.start(0)
motorpwm1.ChangeDutyCycle(100)
motorpwm3.start(0)
motorpwm3.ChangeDutyCycle(100)

# Setup pins for right motor power
rightpwd_in1_pin = 26
rightpwd_in2_pin = 23
GPIO.setup(rightpwd_in1_pin, GPIO.OUT)
GPIO.setup(rightpwd_in2_pin, GPIO.OUT)
motorpwm2 = GPIO.PWM(rightpwd_in1_pin,100)
motorpwm4 = GPIO.PWM(rightpwd_in2_pin,100)
motorpwm2.start(0)
motorpwm2.ChangeDutyCycle(100)
motorpwm4.start(0)
motorpwm4.ChangeDutyCycle(100)

# Set the engines to move forward
GPIO.output(leftmotor_in1_pin, False)
GPIO.output(leftmotor_in2_pin, True)
GPIO.output(rightmotor_in1_pin, False)
GPIO.output(rightmotor_in2_pin, True)

time.sleep(10)

motorpwm1.stop()
motorpwm2.stop()
motorpwm3.stop()
motorpwm4.stop()

GPIO.cleanup()
