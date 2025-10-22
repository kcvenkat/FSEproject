import RPi.GPIO as GPIO
import time
import threading

buzzer_pin = 17
buzzer_pwm = None
buzzing = False   # Flag to control buzzing
stop_threads = False  # Flag to stop the thread cleanly

def setup():
    GPIO.setmode(GPIO.BOARD)
    global buzzer_pwm
    GPIO.setup(buzzer_pin, GPIO.OUT)
    buzzer_pwm = GPIO.PWM(buzzer_pin, 2000)
    buzzer_pwm.start(0)

def buzzer_cycle():
    """Background thread function: continuously buzz while 'buzzing' is True."""
    global buzzing
    while not stop_threads:
        if buzzing:
            buzzer_pwm.ChangeDutyCycle(50)  # Turn buzzer on
            time.sleep(0.2)                 # On duration
            buzzer_pwm.ChangeDutyCycle(0)   # Turn buzzer off
            time.sleep(0.2)                 # Off duration
        else:
            time.sleep(0.1)                 # Short wait to prevent busy loop

def loop():
    global buzzing
    while True:
        user_input = input("1 to start buzzing, 0 to stop, q to quit: ").strip().lower()

        if user_input == '1':
            buzzing = True
        elif user_input == '0':
            buzzing = False
        elif user_input == 'q':
            buzzing = False
            break

def destroy():
    global stop_threads
    stop_threads = True
    if buzzer_pwm:
        buzzer_pwm.stop()
    GPIO.cleanup()

if __name__ == "__main__":
    setup()
    # Start background thread once
    threading.Thread(target=buzzer_cycle, daemon=True).start()
    try:
        loop()
    finally:
        destroy()
