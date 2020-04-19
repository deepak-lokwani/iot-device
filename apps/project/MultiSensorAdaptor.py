'''
Created on 04-Apr-2020

@author: deepa
'''
# from labs.module08.MqttClientConnector import MqttClientConnector
'''
this python script starts the entire Humidity and Temperature Handling process here. This is the main/start process
'''

from project import UltrasonicSensorAdaptorTask
from project import PirSensorAdaptorTask
from project import MultiActuatorApp

from time import sleep

class MultiSensorAdaptor(object):
    
    '''
    instance of temperature and humidity Emulators created with threshold value
    '''
    
    def okGoogle(self):
        
       
        
        Ultrasonicsimulator = UltrasonicSensorAdaptorTask.UltrasonicSensorAdaptorTask()
        Ultrasonicsimulator.start()
        Ultrasonicsimulator.setEmulator(True)
        sleep(3)
        multiActuatorApp = MultiActuatorApp.MultiActuatorApp()
        multiActuatorApp.start()
        sleep(3)
        PirSimulator = PirSensorAdaptorTask.PirSensorAdaptorTask()
        PirSimulator.start()
        PirSimulator.setEmulator(True)
        
        

        Ultrasonicsimulator.join()
        PirSimulator.join()
        multiActuatorApp.join()
        
        while(True):
            sleep(3)
