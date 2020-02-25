'''
Created on 23-Feb-2020

@author: deepa
'''
from labs.common.SensorData import SensorData

class SensorDataListener(object):
    
    def __init__(self):
        #default constructor
        
        '''
        method to display the message on console
        '''
        
    def OnMessage(self):
        sensorData = SensorData()
        print('SensorData sent to DBMS')
