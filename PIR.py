import RPi.GPIO as GPIO
import time

import pymongo
from pymongo import MongoClient
client = MongoClient('mongodb://admin:admin@ds237979.mlab.com:37979/apollo-dev')
db=client['apollo-dev']


def PIR_reading():
    GPIO.setmode(GPIO.BCM)

    pin_to_circuit1 = 18

    GPIO.setup(pin_to_circuit1, GPIO.IN)

    GPIO.setwarnings(False)

    r = 0

    r += 1
##    time.sleep(2)
    a = float(GPIO.input(pin_to_circuit1))
##    print(a)
    #Store in database 
    data={"uuid": "1", "entry_num": r, "motion": bool(a)}
    result=db.motion.insert(data)
    return a



