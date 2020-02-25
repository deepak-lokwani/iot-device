'''
Created on 08-Feb-2020

@author: deepak_lokwani
'''

'''
this class is used to update the actuator  attributes and further actuate the LED Matrix on the SenseHat 
This class also actuates/starts the thread of a  SenseHatLedActivator class 
'''

from labs.common import ActuatorData
from labs.module05 import SenseHatLedActivator
class TempActuatorAdaptor(object):
    '''
    Actuator emulator, process the actuator data
    @param actuatorData: instance of actuator data class
    @param senseHat: instance of SenseHatledActivator class   

    '''
    actuatorData = None
    senseHat = None
    sensorType = 'None'
    

    def __init__(self):
        '''
        Constructor
        '''
        self.actuatorData = ActuatorData.ActuatorData()
        self.senseHat = SenseHatLedActivator.SenseHatLedActivator()
        #start my sensehat thread
        self.senseHat.start()
        
        
    def updateActuator(self,actuatorData, sensorType):
        '''
        compare actuator data and sensor type received and accordingly show the message on the sensehat LED Matrix
        '''
        if(sensorType == 'temp'):
            
            #Checks if  my actuator is updated or not. Proceeds only when there is a  change in the actuator data to avoid the repetition 
            if(self.actuatorData != actuatorData):
                #Checks for the positive change in the temperature data value and decrements the temperature
                if(actuatorData.getValue() > 0):
                    self.senseHat.setEnableLedFlag(True)
                    self.senseHat.setDisplayMessage('Dec temp by: %.2f'  %(actuatorData.getValue()))
                    self.actuatorData.updateData(actuatorData)
                    return True
            
                #checks for the negative change of  temperature value and increments the temperature
                elif(actuatorData.getValue() < 0):
                    self.senseHat.setEnableLedFlag(True)
                    self.senseHat.setDisplayMessage('Inc temp by: %.2f'  %(actuatorData.getValue()));
                    self.actuatorData.updateData(actuatorData)
                    return True
        #checks for the sensordata coming from Sensehat library    
        elif(sensorType == 'humidSH'):
            self.senseHat.setEnableLedFlag(True)
            self.senseHat.setDisplayMessage('SH: %.2f' %(actuatorData))
            return True
        #checks for the sensor data coming from I2C bus    
        elif(sensorType == 'humidI2C'):
            self.senseHat.setEnableLedFlag(True)
            self.senseHat.setDisplayMessage('I2C: %.2f' %(actuatorData))
            return True
        
