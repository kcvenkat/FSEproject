import RPi.GPIO as GPIO
from time import sleep

MOTION_PIN = 12
BUZZER_PIN = 11

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(MOTION_PIN, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

    GPIO.setup(BUZZER_PIN, GPIO.OUT, initial=GPIO.HIGH)

    print("Calibrating PIR...")
    sleep(5)
    print("Ready!")

def beep(duration=0.1):
    GPIO.output(BUZZER_PIN, GPIO.LOW)
    sleep(duration)
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

def loop():
    while True:
        motion = GPIO.input(MOTION_PIN)
        print(motion)
        if motion:
            beep(0.1)
            sleep(0.1)
        else:
            GPIO.output(BUZZER_PIN, GPIO.HIGH)
            sleep(0.02)

def destroy():
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    try:
        loop()
    finally:
        destroy()
