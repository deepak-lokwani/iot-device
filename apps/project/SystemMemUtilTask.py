'''
Created on 30-Mar-2020

@author: deepa
'''
import psutil

'''
This class is responsible for getting the memory 
utilization of the gateway device computer. It 
returns a value in terms of a percentage of the 
total capacity of the heap memory.
'''


class SystemMemUtilTask():
    
    def getDataFromSensor(self):
        memUtil = psutil.virtual_memory().percent
        return memUtil