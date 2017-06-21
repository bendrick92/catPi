import RPi.GPIO as GPIO
import time


class ServoManager:

    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        self.pwm = GPIO.PWM(18, 100)

    def run(self):
        self.pwm.start(10)
        time.sleep(.75)
        self.pwm.stop()

    def cleanup(self):
        GPIO.cleanup()