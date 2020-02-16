'''
Created on 08-Feb-2020

@author: deepak
'''

'''
this class is used to Activate/actuate the LED matrix on the SENSEHAT for user based on the threshold conditions of the sensor  output
'''
from time import sleep
from sense_hat import SenseHat
import threading

class SenseHatLedActivator(threading.Thread):
    '''
    This class is designed to display the appropriate message on SenseHat 
    @param enableLed: boolean to set the led flag
    @param sleepTimeLed: Thread sleep duration
    @param senseHatInst: SensorHat instance
    @param screenMsg: The message to display     
    '''
    enableLed = False
    sleepTimeLed = 1
    rotateDeg = 270
    senseHatInst = None
    screenMsg = None

    def __init__(self):
        '''
        Constructor
        '''
        
        '''
        This method is used to set the display message and set up the Sensehat LED Matrix 
        '''
        super(SenseHatLedActivator, self).__init__()
        if self.sleepTimeLed > 0:
            self.sleepTimeLed = self.sleepTimeLed
        if self.rotateDeg >= 0:
            self.rotateDeg = self.rotateDeg
            self.senseHatInst = SenseHat()
            self.senseHatInst.set_rotation(self.rotateDeg)
            
            
    def run(self):
        '''
        function called when thread starts
        this method is used to display the message based on the input conditions
        '''
        while True:
            if self.enableLed:
                if self.screenMsg != None:
                    self.senseHatInst.show_message(str(self.screenMsg), scroll_speed = 0.05)
                else:
                    self.senseHatInst.show_letter(str('X'))
                sleep(self.sleepTimeLed)
                self.senseHatInst.clear()
            sleep(self.sleepTimeLed)
            
            
    def getSleepTimeLed(self):
        return self.sleepTimeLed
    
    
    def setEnableLedFlag(self, enable):
        self.senseHatInst.clear()
        self.enableLed = enable
        
        
    def setDisplayMessage(self, msg):
        self.screenMsg = msg
            