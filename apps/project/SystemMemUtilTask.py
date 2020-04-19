'''
Created on 30-Mar-2020

@author: deepa
'''
import psutil


class SystemMemUtilTask():
    
    def getDataFromSensor(self):
        memUtil = psutil.virtual_memory().percent
        return memUtil