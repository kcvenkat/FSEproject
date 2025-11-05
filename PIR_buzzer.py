import RPi.GPIO as GPIO
from time import sleep
motion_pin = 12
buzzer_pin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motion_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    sleep(5)

def beep(sleep_time):
    GPIO.output(buzzer_pin, GPIO.LOW)
    sleep(sleep_time)
    GPIO.output(buzzer_pin, GPIO.HIGH)
    sleep(sleep_time)

def loop():
    while True:
        motion = GPIO.input(motion_pin)
        if motion:
            beep(0.1)
        else:
            GPIO.output(buzzer_pin, GPIO.HIGH)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    finally:
        destroy()
