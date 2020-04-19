'''
Created on 30-Mar-2020

@author: deepak lokwani

NUID: 001316769
'''
from project import SystemPerformanceApp
from project import MultiSensorAdaptor

systemPerformanceApp = SystemPerformanceApp.SystemPerformanceApp()
systemPerformanceApp.startHere()
 
multiSensorAdaptor = MultiSensorAdaptor.MultiSensorAdaptor()
multiSensorAdaptor.okGoogle()


