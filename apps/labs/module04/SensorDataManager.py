'''
Created on 08-Feb-2020

@author: deepa
'''

'''
This class  manages and process all the sensor data that is received as per the user-defined/configured threshold settings
'''

from labs.common import ActuatorData
from labs.common import ConfigUtil
from labs.module04 import MultiActuatorAdaptor
from labs.module02 import SMTPClientConnector

class SensorDataManager(object):
    
    actuator = ActuatorData.ActuatorData()
    connector = SMTPClientConnector.SMTPClientConnector
    
    
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfig()
        self.actuatorAdaptor = MultiActuatorAdaptor.TempActuatorAdaptor()
 
    
    def handleSensorData(self, curTemp):
        '''
        this method  handles all the sensor data and updates the actuator settings
        '''
        self.nominalTemp = float(self.config.getProperty(self.config.configConst.CONSTRAINED_DEVICE, self.config.configConst.NOMINAL_TEMP))
       
        #checks if my current temperature is greater than nominal temperature
        if(curTemp > self.nominalTemp):
            # set the Actuator data according to current temperature
            self.actuator.setCommand(ActuatorData.COMMAND_ON)
            self.actuator.setStateData('Decrease')
            self.actuator.setValue(curTemp - self.nominalTemp)
            self.actuatorAdaptor.updateActuator(self.actuator)
#             self.connector.publishMessage('Excessive Temperature Alert', self.actuator)
            
        #checks if my current temperature is lesser than nominal temperature
        elif(curTemp < self.nominalTemp):
            # set the Actuator data according to current temperature
            self.actuator.setCommand(ActuatorData.COMMAND_OFF)
            self.actuator.setStateData('Increase')
            self.actuator.setValue(curTemp - self.nominalTemp)
            self.actuatorAdaptor.updateActuator(self.actuator)
#             self.connector.publishMessage('Excessive Temperature Alert', self.actuator)
