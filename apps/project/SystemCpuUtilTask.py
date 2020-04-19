'''
Created on 30-Mar-2020

@author: deepa
'''
import psutil


class SystemCpuUtilTask():
    
    def getDataFromSensor(self):
        cpuUtil = psutil.cpu_percent(0, False)
        return cpuUtil
        
