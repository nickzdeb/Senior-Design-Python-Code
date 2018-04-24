import RPi.GPIO as GPIO
import time
import datetime

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

#ss_relay_1 = 17 #solid state relay pin 1
#GPIO.setup(ss_relay_1, GPIO.OUT)

#while(True):
    #GPIO.output(ss_relay_1, GPIO.HIGH)
    #time.sleep(3)
#GPIO.output(ss_relay_1, GPIO.HIGH)
    #time.sleep(3)

pin_to_circuit0 = 14 #Left
pin_to_circuit1 = 26 #Right
left_led = 15 #left led
right_led = 19
#pin_to_circuit2 = 19

GPIO.setup(pin_to_circuit0, GPIO.IN)
GPIO.setup(pin_to_circuit1, GPIO.IN)
GPIO.setup(left_led, GPIO.OUT)
GPIO.setup(right_led, GPIO.OUT)

#GPIO.setwarnings(False)

while(True):
    #GPIO.output(pin_to_circuit0, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit0, GPIO.LOW)

    a = float(GPIO.input(pin_to_circuit0))
    print("Left: ", a)

    if a == 1:
        GPIO.output(left_led, GPIO.HIGH)
    else:
        GPIO.output(left_led, GPIO.LOW)
    
    b = float(GPIO.input(pin_to_circuit1))
    print("Right: ", b)

    if b == 1:
        GPIO.output(right_led, GPIO.HIGH)
    else:
        GPIO.output(right_led, GPIO.LOW)
    
    time.sleep(.2)

#GPIO.setup(pin_to_circuit1, GPIO.IN)


#GPIO.output(pin_to_circuit2, GPIO.HIGH)
    #time.sleep(1)
    #GPIO.output(pin_to_circuit2, GPIO.LOW)


#print(now)
