import RPi.GPIO as GPIO
import time

class PIRBuzzer:
    def __init__(self, init):
        self.init = init

    def check_motion(self):
        while True:
            if GPIO.input(self.init.motion_pin):
                GPIO.output(self.init.buzzer_pin, False)
                print("Motion detected!")
                time.sleep(0.5)
                GPIO.output(self.init.buzzer_pin, True)
            time.sleep(0.01)
