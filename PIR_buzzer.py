import RPi.GPIO as GPIO
from time import sleep
motion_pin = 12
buzzer_pin = 11

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motion_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    global buzzer_pwm
    buzzer_pwm = GPIO.PWM(buzzer_pin, 1000)
    buzzer_pwm.start(0)

def buzzer_on(intensity, sleep_time):
    buzzer_pwm.ChangeDutyCycle(intensity)
    sleep(sleep_time)
    buzzer_pwm.ChangeDutyCycle(0)
    sleep(sleep_time)

def buzzer_off():
    buzzer_pwm.ChangeDutyCycle(0) 

def loop():
    while True:
        motion = GPIO.input(motion_pin)
        print(motion)
        if motion == 1:
            buzzer_on(50, 0.5)
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
