'''
Created on 30-Mar-2020

@author: deepa
'''

from project import SystemPerformanceAdaptor 
'''
This class is repsonsible for  
used to start a thread of the  system performance Adaptor 
in order to monitor regularly the system performance paramters
'''
class SystemPerformanceApp(object):
     
    def startHere(self):
 
        #creating an instance of SystemPerformanceAdaptor
        systemPerformanceAdaptor = SystemPerformanceAdaptor.SystemPerformanceAdaptor()
         
        #set true to the begin for threading
        systemPerformanceAdaptor.setAdaptor(True)
         
        #start the thread
        systemPerformanceAdaptor.start()