import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

pwm = GPIO.PWM(18, 100)

pwm.start(10)
time.sleep(.75)

pwm.stop()
GPIO.cleanup()