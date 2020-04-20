'''
Created on 30-Mar-2020

@author: deepak lokwani

NUID: 001316769
'''
from project import SystemPerformanceApp
from project import MultiSensorAdaptor

'''
This is a python script used to run two threaded classes. 
Two threads one for the data manager and the other for the system performance.
This is my main class. It starts the process at the constrained device end. 

'''

systemPerformanceApp = SystemPerformanceApp.SystemPerformanceApp()
systemPerformanceApp.startHere()
 
multiSensorAdaptor = MultiSensorAdaptor.MultiSensorAdaptor()
multiSensorAdaptor.startHere()


