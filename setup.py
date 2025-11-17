import RPi.GPIO as GPIO
import time

class Initialize:
    def __init__(self, trig_pin, echo_pin, buzzer_pin, motor_pin, motion_pin):
        GPIO.setmode(GPIO.BOARD)

        self.trig_pin = trig_pin
        self.echo_pin = echo_pin
        self.buzzer_pin = buzzer_pin
        self.motor_pin = motor_pin
        self.motion_pin = motion_pin

        #pin initialization
        GPIO.setup(self.trig_pin, GPIO.OUT)
        GPIO.setup(self.echo_pin, GPIO.IN)
        GPIO.setup(self.buzzer_pin, GPIO.OUT)
        GPIO.setup(self.motor_pin, GPIO.OUT)
        GPIO.setup(self.motion_pin, GPIO.IN)

        #pwm initialization for motor
        self.motor_pwm = GPIO.PWM(motor_pin, 1000)
        self.motor_pwm.start(0)

        # Initialize outputs to low
        GPIO.output(self.trig_pin, False)
        GPIO.output(self.buzzer_pin, True)
        GPIO.output(self.motor_pin, False)

        #PIR calibration time
        print("Calibrating...")
        time.sleep(5)
        print("Done!")
        print()

    def destroy(self):
        self.motor_pwm.stop()
        GPIO.cleanup()
