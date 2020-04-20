'''
Created on 04-Apr-2020

@author: deepa
'''
# from labs.module08.MqttClientConnector import MqttClientConnector
'''
this python script starts the entire PIR Sensor and
 Ultrasonic Sensor Handling process here. 
Three threads for the 2 sensors and one actuators
 is started  here nad then joined back
'''

from project import UltrasonicSensorAdaptorTask
from project import PirSensorAdaptorTask
from project import MultiActuatorApp

from time import sleep


class MultiSensorAdaptor(object):
    
    '''
    instance of temperature and humidity Emulators created with threshold value
    '''
    
    def startHere(self):
        
        Ultrasonicsimulator = UltrasonicSensorAdaptorTask.UltrasonicSensorAdaptorTask()
        Ultrasonicsimulator.start()
        Ultrasonicsimulator.setEmulator(True)
        sleep(4)
        multiActuatorApp = MultiActuatorApp.MultiActuatorApp()
        multiActuatorApp.start()
        sleep(4)
        PirSimulator = PirSensorAdaptorTask.PirSensorAdaptorTask()
        PirSimulator.start()
        PirSimulator.setEmulator(True)
        sleep(4)
        
        Ultrasonicsimulator.join()
        PirSimulator.join()
        multiActuatorApp.join()
        
        while(True):
            sleep(4)
