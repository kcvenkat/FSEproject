#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# Define GPIO pins
TRIG = 11       # GPIO pin connected to Trig of Ultrasonic Sensor
ECHO = 12       # GPIO pin connected to Echo of Ultrasonic Sensor
BuzzerPin = 13  # GPIO pin connected to Buzzer

# Global PWM object
buzzer_pwm = None

def setup():
    """ Setup the GPIO pins for the ultrasonic sensor and buzzer """
    global buzzer_pwm
    GPIO.setmode(GPIO.BOARD)
    
    # Setup for ultrasonic sensor
    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.setup(ECHO, GPIO.IN)
    
    # Setup for buzzer with PWM
    GPIO.setup(BuzzerPin, GPIO.OUT)
    buzzer_pwm = GPIO.PWM(BuzzerPin, 2000)  # Start with 2000 Hz frequency
    buzzer_pwm.start(0)  # Start with 0% duty cycle (off)

def distance():
    """ Measure the distance using the ultrasonic sensor """
    GPIO.output(TRIG, 0)
    time.sleep(0.000002)
    GPIO.output(TRIG, 1)
    time.sleep(0.00001)
    GPIO.output(TRIG, 0)
    
    while GPIO.input(ECHO) == 0:
        pass
    time1 = time.time()
    
    while GPIO.input(ECHO) == 1:
        pass
    time2 = time.time()

    duration = time2 - time1
    return (duration * 340 / 2) * 100  # Convert to centimeters

def buzzer_on():
    """ Turn the buzzer on """
    buzzer_pwm.ChangeDutyCycle(50)  # 50% duty cycle

def buzzer_off():
    """ Turn the buzzer off """
    buzzer_pwm.ChangeDutyCycle(0)  # 0% duty cycle

def beep(duration):
    """ Make the buzzer beep for a specified duration """
    buzzer_on()
    time.sleep(duration)
    buzzer_off()
    time.sleep(duration)

def loop():
    """ Main loop that checks the distance and controls the buzzer """
    while True:
        dis = distance()
        print(f'{dis:.2f} cm')  # Print distance measurement

        if dis < 5:  # If the object is within 5 cm, buzz continuously at high pitch
            buzzer_pwm.ChangeFrequency(3000)  # High frequency for close proximity
            buzzer_on()
        elif dis < 30:  # If within 30 cm, beep with decreasing interval and increasing pitch
            # Calculate beep interval - shorter beeps as object gets closer
            beep_interval = max(0.05, (dis - 5) / 100.0)  # Minimum 50ms beeps
            
            # Change frequency based on distance - higher pitch when closer
            freq = int(500 + (30 - dis) * 100)  # Range from 500Hz to 3000Hz
            buzzer_pwm.ChangeFrequency(freq)
            
            beep(beep_interval)
        else:
            buzzer_off()  # Turn off buzzer if object is far
        
        time.sleep(0.1)  # Shorter delay for more responsive detection

def destroy():
    """ Cleanup function to reset GPIO settings """
    if buzzer_pwm:
        buzzer_pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
