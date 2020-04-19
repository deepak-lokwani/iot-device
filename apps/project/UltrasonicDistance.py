'''
Created on 01-Apr-2020

@author: deepa
'''
import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

TRIG = 23
ECHO = 24

print('Distance Measurement In Progress')

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def measure():
    
    GPIO.output(TRIG, False)
    print('Waiting For Sensor To Settle')
    time.sleep(2)
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)
    
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
        
    while GPIO.input(ECHO)==1:
        pulse_end = time.time() 
    
    pulse_start = time.time() 
    sleep(0.1)
    pulse_end = time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance 
    
try:
    
    while True:
        dist = measure()
        print('Distance = ' + str(dist))
        sleep(1)
        
except KeyboardInterrupt:
    GPIO.clear()
        
        