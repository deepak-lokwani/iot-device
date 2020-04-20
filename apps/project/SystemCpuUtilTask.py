'''
Created on 30-Mar-2020

@author: deepa
'''
import psutil
'''
This class is responsible for getting the cpu utilization 
of the constrained device computer. It returns a value 
in terms of a percentage of the capacity of the processor
'''

class SystemCpuUtilTask():
    
    def getDataFromSensor(self):
        cpuUtil = psutil.cpu_percent(0, False)
        return cpuUtil
        
