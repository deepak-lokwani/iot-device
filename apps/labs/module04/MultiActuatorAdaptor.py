'''
Created on 08-Feb-2020

@author: deepak
'''

'''
this class is used to update the actuator  attributes and further actuate the LED Matrix on the SenseHat 
This class also actuates/starts the thread of a  SenseHatLedActivator class 
'''

from labs.common import ActuatorData
from labs.module04 import SenseHatLedActivator
class TempActuatorAdaptor(object):
    '''
    Actuator emulator, process the actuator data
    @param actuatorData: instance of actuator data class
    @param senseHat: instance of SenseHatledActivator class   

    '''
    actuatorData = None
    senseHat = None
    

    def __init__(self):
        '''
        Constructor
        '''
        self.actuatorData = ActuatorData.ActuatorData()
        self.senseHat = SenseHatLedActivator.SenseHatLedActivator()
        #start my sensehat thread
        self.senseHat.start();
        
        
    def updateActuator(self,actuatorData):
        '''
        compare actuator data received and according show the message on the sensehat
        '''
        #Checks if  my actuator is updated or not. Proceeds only when there is a  change in the actuator data to avoid the repetition 
        if(self.actuatorData != actuatorData):
            #Checks for the positive change in the temperature data value and decrements the temperature
            if(actuatorData.getValue() > 0):
                self.senseHat.setEnableLedFlag(True)
                self.senseHat.setDisplayMessage('Decrement  the temperature by :' + str(actuatorData.getValue()))
                #print('Decrement the temperature by:' + str(actuatorData.getValue()))
                self.actuatorData.updateData(actuatorData)
            
            #checks for the negative change of  temperature value and increments the temperature
            elif(actuatorData.getValue() < 0):
                self.senseHat.setEnableLedFlag(True)
                self.senseHat.setDisplayMessage('Increament the temperature by :' + str(actuatorData.getValue()));
                #print('Increment the temperature by:' + str(abs(actuatorData.getValue())))
                self.actuatorData.updateData(actuatorData)
        
