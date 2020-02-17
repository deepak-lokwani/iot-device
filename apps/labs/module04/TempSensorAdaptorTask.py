'''
Created on 08-Feb-2020

@author: deepak
'''

'''
This class is used to setup the task of getting the Temperature sensor data values using the SenseHat 
and send it further to the data processing classes like sending SMTP and Data management classes
'''
import threading
from labs.common import SensorData
from labs.module02 import SMTPClientConnector
from labs.common import ConfigUtil
from labs.common import ActuatorData
from labs.module04 import MultiActuatorAdaptor, SensorDataManager
from time import sleep
from sense_hat import SenseHat
import random
import logging

sensorDataMgr = SensorDataManager.SensorDataManager()

class TempSensorAdaptorTask(threading.Thread):
    
    #create an instance variable for configutil
    config = ConfigUtil.ConfigUtil()
    
    
    
    def __init__(self,alertdiff):
        '''
        constructor
        @param sensorData: sensorData class instance
        @param connector: instance of smtpClientConnector class
        @param alertDiff: the threshold value for sending alert message
        @param enableEmulator:boolean state of the emulator, initialized to False
        @param timeInterval:time in seconds between each data generation/collection
        @param lowValue:lowest value of the temperature achieved/expected
        @param highValue: highest value of the temperature expected/achieved
        @param curTemp: current value of the temperature       
        '''
        threading.Thread.__init__(self)
        self.enableEmulator = False
        logging.basicConfig(level=logging.INFO , format='    %(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S' )

        self.timeInterval = int(self.config.getProperty(self.config.configConst.CONSTRAINED_DEVICE, self.config.configConst.POLL_CYCLES_KEY))
        self.alertDiff = alertdiff
        self.nominalTemp = int(self.config.getProperty(self.config.configConst.CONSTRAINED_DEVICE, self.config.configConst.NOMINAL_TEMP))
        self.lowValue = 0
        self.highValue = 30
        self.curTemp = 0
        self.prevTemp = 0.0
        self.prevTempFlag = False
        self.SenseHat = SenseHat()
        self.sensorData = SensorData.SensorData()
        self.connector =  SMTPClientConnector.SMTPClientConnector()
              
        self.actuator = ActuatorData.ActuatorData()
        self.actuatorAdaptor = MultiActuatorAdaptor.TempActuatorAdaptor()
        
      
    
    def setEmulator(self,boolean):
        '''
        set the boolean value to start the emulator
        '''
        self.enableEmulator = boolean;
        
    
    def run(self):
        '''
        Thread.run default function called when thread 'starts'
        when running, it will generate the random numbers and will update 
        the sensor data registers accordingly. 
        further whenever the threshold is achieved, it will push an email along with logging it to the console
        '''
        threading.Thread.run(self)
        while True:
            if(self.enableEmulator):
                #self.curTemp = random.uniform(float(self.lowValue),float(self.highValue))
                self.curTemp = self.SenseHat.get_temperature()  #get temperature from SenseHat
                self.sensorData.addValue(self.curTemp)
                print('__________________________________________________')
                print(str(self.sensorData.getSensorData()))
                if(abs(self.curTemp - self.sensorData.getAvgValue())>=self.alertDiff):
                    logging.info('/n Excessive Temperature with a difference > ' + str(self.alertDiff) + '/nTriggering Alert')
                    print('Excessive Temperature with a difference > ' + str(self.alertDiff) + '/nTriggering Alert')
                    
                    self.connector.publishMessage('Temperature Alert message', self.sensorData.getSensorData())
                    logging.info('/nEmail Sent')
                    print('Email Sent')
                
                if(self.prevTempFlag == False):
                    self.prevTemp = self.curTemp
                    self.prevTempFlag = True
                    
                if (self.prevTempFlag ==True):
                    if(self.prevTemp != self.curTemp): 
                        sensorDataMgr.handleSensorData(self.sensorData.getValue(), 'temp')
                #sleep(self.timeInterval)
                sleep(10)