'''
Created on 04-Apr-2020

@author: deepa
'''


'''
This class is used to setup the task of getting the Temperature sensor data values using the SenseHat 
and send it further to the data processing classes like sending SMTP and Data management classes
'''

import threading
from project.commons import SensorData
from project.protocols import SMTPClientConnector
from labs.common import DataUtil
from project import UltrasonicSensorEmulator as UsEmulator
from time import sleep
import logging
# from labs.module08.MqttClientConnector import MqttClientConnector as mqtt08
from project.commons.MqttClientConnector import MqttClientConnector as mqtt08

class UltrasonicSensorAdaptorTask(threading.Thread):
    
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

        self.lowValue = 4.0
        self.highValue = 300.0
        self.curDist = 0.0
        
        self.prevDist = 0.0
        self.lowValueCounter = 0
        self.repeatValueCounter = 0
        self.prevDistFlag = False
        self.repeatValueFlag = False
        self.lowValueFlag = False
        
        self.sensorData = SensorData.SensorData()
        self.connector =  SMTPClientConnector.SMTPClientConnector()
        self.mqtt08 =  mqtt08()
        self.mqtt08.connect(None, None)
        self.sensorData.setName("US Attribute")
    
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
                self.curDist = UsEmulator.getDistance()
                self.sensorData.addValue(self.curDist)
                
                if(self.curDist     >=   self.highValue):
#                     logging.info('greater than range ignore' )
                    pass
                    
                elif(self.curDist     <=    self.lowValue):
#                     logging.info('lesser than range ' )
                    self.lowValueCounter +=1
                    if(self.lowValueCounter > 2  ):
#                         logging.info('cleaning required SHOOT MAIL')
                        pass
                self.sensorData.setUSLowValueFlag(True)

                if(self.prevDistFlag == False):
                    self.prevDist = self.curDist
                    self.prevDistFlag = True
                    jsonSensorData = DataUtil.DataUtil().toJsonFromSensorData(self.sensorData)
                    self.mqtt08.publishMessage("USFromSensor", jsonSensorData, 2)
                     
                elif(self.prevDistFlag == True):
                    if(self.prevDist == self.curDist):
                        self.repeatValueCounter = self.repeatValueCounter + 1
                        if(self.repeatValueCounter == 10):
                            self.sensorData.setUSRepeatedValueFlag(True)
#                             logging.info('values frozen send SMTP')
                    
                    elif(self.prevDist != self.curDist): 
                        self.mqtt08.publish_message(self.sensorData, "USFromSensor")
                sleep(10)