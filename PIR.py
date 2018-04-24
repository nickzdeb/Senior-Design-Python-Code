import RPi.GPIO as GPIO
import time


def PIR_reading():
    GPIO.setmode(GPIO.BCM)

    pin_to_circuit1 = 18

    GPIO.setup(pin_to_circuit1, GPIO.IN)

    GPIO.setwarnings(False)
    
    a = float(GPIO.input(pin_to_circuit1))

    return a



