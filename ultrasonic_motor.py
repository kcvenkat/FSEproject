import RPi.GPIO as GPIO
import time

class UltMotor:
    def __init__(self, init):
        self.init = init
    
    def distance(self, timeout = 0.5):
        trig_pin = self.init.trig_pin
        echo_pin = self.init.echo_pin

        GPIO.output(trig_pin, GPIO.LOW)
        time.sleep(0.00001)
        GPIO.output(trig_pin, GPIO.HIGH)
        time.sleep(0.00001)

        start_time = time.time()
        while GPIO.input(echo_pin) == 0: #while echo_pin is set to GPIO.LOW
            if time.time() - start_time > timeout:
                return -1
        time1 = time.time()
        
        start_time = time.time()
        while GPIO.input(echo_pin) == 1: #While echo_pin is set to GPIO.HIGH
            if time.time() - start_time > timeout:
                return -1

        time2 = time.time()
        duration = time2 - time1
        distance_cm = (duration * 340 / 2) * 100
        return distance_cm
    
    def set_motor_speed(self, duty_cycle):
        self.init.motor_pwm.ChangeDutyCycle(duty_cycle)

    def stop_motor(self):
        self.init.motor_pwm.ChangeDutyCycle(0)
        GPIO.output(self.init.motor_pin, GPIO.LOW)

    def vibrate_motor(self, intensity = 50, sleep_time = 0.5):
        self.set_motor_speed(intensity)
        time.sleep(sleep_time)
        self.set_motor_speed(0)
        time.sleep(sleep_time)
