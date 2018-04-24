import time
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

# Function used to convert binary to digit
def convert_to_tens(digit_array):
   result = 0
   length = len(digit_array)
   t0 = 0
   while (t0<length):
      t1 = digit_array[t0]

      t2 = length - 1
      t2 = t2 - t0
      while(t2>0):
         t1 = t1 * 2
         t2 = t2 - 1
      result = result + t1
      t0 = t0 + 1
   return result

# Function used to read data from light sensor
def lightReading():
   
   # Set pins
   GPIO.setmode(GPIO.BCM)
   pin_to_circuit1 = 16     #clock signal
   pin_to_circuit2 = 21     #CS
   pin_to_circuit3 = 20     #Data

   data = []                # Create space to hold data

   # GPIO setup
   GPIO.setup(pin_to_circuit1, GPIO.OUT)
   GPIO.setup(pin_to_circuit2, GPIO.OUT)
   GPIO.setup(pin_to_circuit3, GPIO.IN)
   
   # Initialize the sensor
   GPIO.output(pin_to_circuit2, GPIO.HIGH)
   # Give the time for sensor to seattle
   time.sleep(0.5)

    
   for j in range(0,1):
      GPIO.output(pin_to_circuit2, GPIO.LOW)
      for i in range(0,16): 
         time.sleep(0.1)
         GPIO.output(pin_to_circuit1, GPIO.LOW)
         time.sleep(0.1)
         GPIO.output(pin_to_circuit1, GPIO.HIGH)
         data.insert(i,GPIO.input(pin_to_circuit3))
      GPIO.output(pin_to_circuit2, GPIO.HIGH)

   # Formate data
   del data[12:16]
   del data[0:4]
   # Convert Binary to 10s
   answer = convert_to_tens(data)

   return answer
