import time
import threading
import RPi.GPIO as GPIO
from pir_buzzer import PIRBuzzer
from setup import Initialize
from ultrasonic_motor import UltMotor

init = Initialize(
    trig_pin=11,
    echo_pin=12,
    buzzer_pin=15,
    motor_pin=36,
    motion_pin=13
)

pir_buzzer = PIRBuzzer(init)
ult_motor = UltMotor(init)

def ultrasonic_monitor():
    while True:
        dist = ult_motor.distance()
        if dist != -1 and dist <= 275:
            ult_motor.vibrate_motor(50, 0.2)
        elif dist!= -1 and dist <= 600:
            ult_motor.vibrate_motor(50, 0.5)
        else:
            ult_motor.set_motor_speed(0)
            ult_motor.stop_motor()
        time.sleep(0.01)

us_thread = threading.Thread(target = ultrasonic_monitor, daemon= True)
pir_thread = threading.Thread(target = pir_buzzer.check_motion, daemon = True)

pir_thread.start()
us_thread.start()

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    GPIO.cleanup()
    print("Program stopped safely.")
