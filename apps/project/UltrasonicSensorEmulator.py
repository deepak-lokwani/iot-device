'''
Created on 05-Apr-2020

@author: deepa
'''

import random

'''
this is a Ultrasonic Sensor Emulator. It producess the 
random float value imitating a US sensor ranging from 0-500 cm
'''
def getDistance():
        minValue = 0
        maxValue = 500
        distance = round(random.uniform(float(minValue), float(maxValue)),1)
#         print(distance)
        return distance