
'''
Created on 20-Jan-2020

@author: deepak
NUID: 001316769
'''
from labs.module01 import SystemPerformanceAdaptor


systemPerformanceAdaptor = None
#creating an instance of SystemPerformanceAdaptor
systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()

#set true to the begin for threading
systemPerformanceAdaptor.setAdaptor(True)

#start the thread
systemPerformanceAdaptor.start()