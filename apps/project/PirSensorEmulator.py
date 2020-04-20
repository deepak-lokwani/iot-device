'''
Created on 08-Apr-2020

@author: deepa
'''
import random

'''
this is a PIR Sensor Emulator. It producess the random boolean value imitating a PIR sensor
'''

def getBoolean():
        
        PIR = random.choice([True, False])
        return PIR