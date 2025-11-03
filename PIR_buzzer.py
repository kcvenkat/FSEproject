import RPi.GPIO as GPIO
from time import sleep
motion_pin = 12
buzzer_pin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motion_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    GPIO.output(buzzer_pin, GPIO.HIGH)

    print("Calibrating...")
    sleep(5) 
    print("Ready!")

def buzzer_on(sleep_time):
    GPIO.output(buzzer_pin, GPIO.LOW)
    sleep(sleep_time)
    GPIO.output(buzzer_pin, GPIO.HIGH)
    sleep(sleep_time)

def buzzer_off():
    GPIO.output(buzzer_pin, GPIO.HIGH) 

def loop():
    while True:
        motion = GPIO.input(motion_pin)
        print(motion)
        if motion == 1:
            buzzer_on(0.1)
        elif motion == 0:
            buzzer_off()
        else:
            pass

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    finally:
        destroy()
