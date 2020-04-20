'''
Created on 08-Apr-2020

@author: deepa
'''
'''
This class is used to setup the task of getting the 
PIR sensor data values using the emulator 
and send it further to the data processing classes 
like publishing to the Gateway and Data management classes
'''

import threading
from project.commons import SensorData
from project import PirSensorEmulator as pirEmulator
from time import sleep
import logging
from project.commons.MqttClientConnector import MqttClientConnector as mqtt08

class PirSensorAdaptorTask(threading.Thread):
    
    #create an instance variable for configutil
#     config = ConfigUtil.ConfigUtil()
    
    def __init__(self):
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

        self.sensorData = SensorData.SensorData()
        self.sensorData.setName('PIR Attribute')
        self.mqtt08 =  mqtt08()
        self.mqtt08.connect(None, None)        
    
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
                self.curPIR = pirEmulator.getBoolean()
                self.sensorData.addPIRValue(self.curPIR)
                self.mqtt08.publish_message(self.sensorData, "PIRFromSensor")
                sleep(45)