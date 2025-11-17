import RPi.GPIO as GPIO
import time
from pir_buzzer import PIRBuzzer

class Initialize:
    def __init__(self, motion_pin, buzzer_pin):
        self.motion_pin = motion_pin
        self.buzzer_pin = buzzer_pin
        # Set up GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.motion_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        GPIO.output(self.buzzer_pin, True)  # buzzer off initially

# Adjust these pins to match your wiring
MOTION_PIN = 13
BUZZER_PIN = 15

# Initialize
init = Initialize(motion_pin=MOTION_PIN, buzzer_pin=BUZZER_PIN)
pir_buzzer = PIRBuzzer(init)

try:
    print("PIR sensor and buzzer test running...")
    print("Move in front of the sensor to trigger the buzzer.\nPress Ctrl+C to stop.")
    pir_buzzer.check_motion()
except KeyboardInterrupt:
    print("\nExiting test.")
finally:
    GPIO.cleanup()
    print("GPIO cleaned up.")
