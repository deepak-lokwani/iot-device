'''
Created on 08-Feb-2020

@author: deepak
'''

'''
this class holds and updates the actuator  attributes including the state values
'''
import os
from datetime import datetime

# Constants
CMD_OFF = 0
CMD_ON = 1
CMD_RESET = 2


class ActuatorData(object):
    '''
    @param timeStamp:stores current date and time 
    @param name: String: actuator's name
    @param stateData: stores my actuator state data /Telemetry
    @param value: Temperature difference value    
    '''
   
    timeStamp = None
    name = 'Temperature State'
    command = CMD_OFF
    stateData = None
    val = 0.0


    def __init__(self):
        '''
        Constructor
        '''
        self.updateTimeStamp()
        
        
    def getCommand(self):
        return self.command
    
    
    def getName(self):
        return self.name
    
    
    def getStateData(self):
        return self.stateData
    
    
    def getValue(self):
        return self.val
    
    
    def setCommand(self, command):
        self.command = command
        
        
    def setName(self, name):
        self.name = name
        
        
    def setStateData(self, stateData):
        self.stateData = stateData
        
        
    def setValue(self, val):
        self.val = val
        
        
    def updateData(self, data):
        '''
        updates the Actuator data
        '''
        self.command = data.getCommand()
        self.stateData = data.getStateData()
        self.val = data.getValue()
        
        
    def updateTimeStamp(self):
        self.timeStamp = str(datetime.now())
        
        
    def __str__(self):
        outputStr = \
            str(self.name + ':' + \
                os.linesep + '\tTime: ' + self.timeStamp + \
                os.linesep + '\tCommand: ' + str(self.command) + \
                os.linesep + '\tState Data: ' + str(self.stateData) + \
                os.linesep + '\tValue: ' + str(self.val))
        return outputStr
        