import RPi.GPIO as GPIO
import time

motor_pin = 7
trig_pin = 11
echo_pin = 12
motion_pin = 13
buzzer_pin = 15

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(motor_pin, GPIO.OUT)
    GPIO.setup(trig_pin, GPIO.OUT)
    GPIO.setup(echo_pin, GPIO.IN)
    GPIO.setup(motion_pin, GPIO.IN)
    GPIO.setup(buzzer_pin, GPIO.OUT)

    GPIO.output(buzzer_pin, GPIO.LOW)

    global motor_pwm
    motor_pwm = GPIO.PWM(motor_pin, 1000)
    motor_pwm.start(0)

    print("Calibrating")
    time.sleep(30)
    print("Setup Finished")
    print()

def distance():
    GPIO.output(trig_pin, GPIO.LOW)
    time.sleep(0.000002)
    GPIO.output(trig_pin, GPIO.HIGH)
    time.sleep(0.00001)
    GPIO.output(trig_pin, GPIO.LOW)

    timeout = time.time() + 0.02
    while GPIO.input(echo_pin) == 0 and time.time() < timeout:
        pass
    if time.time() >= timeout:
        return None
    time1 = time.time()

    timeout = time.time() + 0.05
    while GPIO.input(echo_pin) == 1 and time.time() < timeout:
        pass
    if time.time() >= timeout:
        return None

    time2 = time.time()
    duration = time2 - time1
    distance_cm = (duration * 340 / 2) * 100
    return distance_cm


def motor_on(intensity, sleep_time):
        motor_pwm.ChangeDutyCycle(intensity)
        time.sleep(sleep_time)
        motor_pwm.ChangeDutyCycle(0)
        time.sleep(sleep_time)

def motor_off():
    motor_pwm.ChangeDutyCycle(0)

def buzzer_on(sleep_time):
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(sleep_time)
    GPIO.output(buzzer_pin, GPIO.LOW)
    time.sleep(sleep_time)

def buzzer_off():
    GPIO.output(buzzer_pin, GPIO.LOW)

def loop():
    while True:
        dis = distance()
        motion = GPIO.input(motion_pin)
        print("Distance:", dis, "Motion:", motion)

        if dis is None:
            continue

        if dis <= 275:
            if motion == 1:
                buzzer_on(0.1)
                motor_on(50, 0.2)
            else:
                motor_on(50, 0.2)
        elif dis <= 600:
            if motion ==1:
                buzzer_on(0.3)
                motor_on(50, 0.5)
            else:
                motor_on(50, 0.5)
        else:
            motor_off()
            buzzer_off()
            time.sleep(0.1)

if __name__ == "__main__":
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
