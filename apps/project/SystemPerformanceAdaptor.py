'''
Created on 30-Mar-2020

@author: Deepak_Lokwani
'''

from time import sleep
from project import SystemCpuUtilTask
from project import SystemMemUtilTask
from project.protocols import UbidotsApiConnector
import logging 
import threading

'''
This is a runnable class used to collect my System 
performance data (CPU and Memory) utilization using 
the libraries. This data is further processed and 
sent to the ubidots cloud platform using HTTPS 
based Ubidots API connector.
'''

class SystemPerformanceAdaptor(threading.Thread):
    
    '''
    constructor
    '''

    def __init__(self):
        threading.Thread.__init__(self)
        self.begin = False
        logging.basicConfig(level=logging.INFO , format='    %(asctime)s %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        
        
    '''
    setting the adaptor switch
    '''

    def setAdaptor(self, S):
        self.begin = S
        
    '''
    printing CPU utilization and the virtual memory utilization using psutil library
    '''

    def run(self):
        while(self.begin):
            cpuUtilObj = SystemCpuUtilTask.SystemCpuUtilTask()
            cpuUtilization = cpuUtilObj.getDataFromSensor()
            memUtilObj = SystemMemUtilTask.SystemMemUtilTask()
            memUtilization = memUtilObj.getDataFromSensor()
            logging.info('----------------System Performance-------------')
            logging.info('***********************************************')
            logging.info('CPU    Utilization = '    +   str(cpuUtilization)) 
            logging.info('Memory Utilization = '    +   str(memUtilization))
            self.ubidots = UbidotsApiConnector.main(cpuUtilization, memUtilization)
            sleep(60)
