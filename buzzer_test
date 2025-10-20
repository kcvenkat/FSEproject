import RPi.GPIO as GPIO

buzzer_pin = 17
buzzer_pwm = None

def setup():
    GPIO.setmode(GPIO.BOARD)
    global buzzer_pwm
    GPIO.setup(buzzer_pin, GPIO.OUT)
    buzzer_pwm = GPIO.PWM(buzzer_pin, 2000)
    buzzer_pwm.start(0)

def buzzer_on():
    buzzer_pwm.ChangeDutyCycle(50)

def buzzer_off():
    buzzer_pwm.ChangeDutyCycle(0)

def loop():
    while True:
        user_input = input("1 if on, 0 if off, q to quit").strip().lower()

        if user_input =='1':
            buzzer_on()
        elif user_input == '0':
            buzzer_off()
        elif user_input == 'q':
            break

def destroy():
    if buzzer_pwm:
        buzzer_pwm.stop()
    GPIO.cleanup()

    
if __name__ == "__main__":
    setup()
    try:
        loop()
    finally:
        destroy()


        

