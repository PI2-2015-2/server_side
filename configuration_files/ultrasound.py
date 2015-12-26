import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)   	# Addressing the GPIO pins

TRIG = 19
ECHO = 13

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def distance():

	GPIO.output(TRIG, False)

	# Wait sensor do settle
	time.sleep(0.1)
	GPIO.output(TRIG,True)
	# wait 10 micro seconds (this is 0.00001 seconds) so the pulse
	# length is 10Us as the sensor expects
	time.sleep(0.00001)
	GPIO.output(TRIG,False)

	while GPIO.input(ECHO) == 0:
		start = time.time()		# Current Time in Seconds

	while GPIO.input(ECHO) == 1:
		stop = time.time()

	return (stop - start) * 17150  #distance in cm
