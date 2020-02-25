'''
Created on 23-Feb-2020

@author: deepa
'''
from labs.common.ActuatorData import ActuatorData

class ActuatorDataListener(object):
    
    def __int__(self):
        #default constructor
    
    
        '''
        OnMessage method to diplay the actuator Data
        '''    
    def OnMessage(self):
        actuatorData = ActuatorData()
        print('Actuator Data sent to DBMS')
