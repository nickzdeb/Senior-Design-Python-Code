import time
import RPi.GPIO as GPIO
import datetime
import pymongo

from pymongo import MongoClient

client = MongoClient('mongodb://admin:admin@ds237979.mlab.com:37979/apollo-dev')
db=client['apollo-dev']

now = datetime.datetime.now()

GPIO.setmode(GPIO.BCM)             # Set GPIO output pins format
GPIO.setwarnings(False)

switch1_isOn = False
switch2_isOn = False

touch_input_left = 14 #touch input pin 1
GPIO.setup(touch_input_left, GPIO.IN) 

touch_input_right = 26 #touch input pin 2
GPIO.setup(touch_input_right, GPIO.IN)


ss_relay_1 = 17 #solid state relay pin 1
GPIO.setup(ss_relay_1, GPIO.OUT) 

ss_relay_2 = 27 #solid state relay pin 2
GPIO.setup(ss_relay_2, GPIO.OUT)

left_led = 15 #left led
GPIO.setup(left_led, GPIO.OUT)

right_led = 19
GPIO.setup(right_led, GPIO.OUT)

GPIO.output(left_led, GPIO.HIGH)
GPIO.output(right_led, GPIO.HIGH)
ls1 = False
ls2 = False
lp = True
rp = True
s1=True
s2=True

def lightControl(light1_state, light2_state, left_prev, right_prev, app_state1, app_state2):
    # get control from app
    try:
        switch1 = db.light_control_1.find().sort('_created_at',-1).limit(1)
        for object in switch1:
            #print ("light control 1 ", object["signal"])
            switch1_isOn = object["signal"]
    except Exception, e:
        print str(e)

    #Switch 2 == right pad
    try:
        switch2 = db.light_control_2.find().sort('_created_at',-1).limit(1)
        for object in switch2:
            #print ("light control 2 ", object["signal"])
            switch2_isOn = object["signal"]
    except Exception, e:
        print str(e)

    #Assume SSR's are off
    ## get input from touch pad
    left_check = GPIO.input(touch_input_left)
    #print("light control left pad: ", left_check)
    right_check = GPIO.input(touch_input_right)
    #print("light control right pad: ",right_check) 

    # control the light
    if switch1_isOn == app_state1:
        light1_state = not light1_state
        app_state1=not app_state1
    if left_check:
        if left_prev:
            light1_state = not light1_state
        left_prev=False
        GPIO.output(left_led, GPIO.LOW)
    else:
        left_prev=True
        GPIO.output(left_led, GPIO.HIGH)


    if switch2_isOn == app_state2:
        light2_state = not light2_state
        app_state2=not app_state2
    if right_check:
        if right_prev:
            light2_state = not light2_state
        right_prev=False
        GPIO.output(right_led, GPIO.LOW)
    else:
        right_prev=True
        GPIO.output(right_led, GPIO.HIGH)

        

    if light1_state:
        GPIO.output(ss_relay_1, GPIO.LOW)
    else:
        GPIO.output(ss_relay_1, GPIO.HIGH)
    if light2_state:
        GPIO.output(ss_relay_2, GPIO.LOW)
    else:
        GPIO.output(ss_relay_2, GPIO.HIGH)
    return light1_state, light2_state, left_prev, right_prev
while True:
    time.sleep(.1)
    ls1,ls2,lp,rp,s1,s2 = lightControl(ls1,ls2,lp,rp,s1,s2)

