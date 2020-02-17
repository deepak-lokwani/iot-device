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
    sensorType = 'None'
    
    def __init__(self):
        self.config = ConfigUtil.ConfigUtil()
        self.config.loadConfig()
        self.actuatorAdaptor = MultiActuatorAdaptor.TempActuatorAdaptor()
 
    
    def handleSensorData(self, curVal, sensorType):
        '''
        this method  handles all the sensor data and updates the actuator settings
        '''
        if(sensorType == 'temp'):
            self.nominalTemp = float(self.config.getProperty(self.config.configConst.CONSTRAINED_DEVICE, self.config.configConst.NOMINAL_TEMP))
       
            #checks if my current temperature is greater than nominal temperature
            if(curVal > self.nominalTemp):
                # set the Actuator data according to current temperature
                self.actuator.setCommand(ActuatorData.CMD_ON)
                self.actuator.setStateData('Decrease')
                self.actuator.setValue(curVal - self.nominalTemp)
                self.actuatorAdaptor.updateActuator(self.actuator, 'temp')
#               self.connector.publishMessage('Excessive Temperature Alert', self.actuator)
            
            #checks if my current temperature is lesser than nominal temperature
            elif(curVal < self.nominalTemp):
                # set the Actuator data according to current temperature
                self.actuator.setCommand(ActuatorData.CMD_OFF)
                self.actuator.setStateData('Increase')
                self.actuator.setValue(curVal - self.nominalTemp)
                self.actuatorAdaptor.updateActuator(self.actuator, 'temp')
#               self.connector.publishMessage('Excessive Temperature Alert', self.actuator)
        #checks for the sensorData coming from the Sensehat API
        elif(sensorType == 'humidSH'):
            self.actuatorAdaptor.updateActuator(curVal, 'humidSH')
        
        #checks for the sensorData coming from the I2C bus    
        elif(sensorType == 'humidI2C'):
            self.actuatorAdaptor.updateActuator(curVal, 'humidI2C')
