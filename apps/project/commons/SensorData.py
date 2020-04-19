'''
Created on 05-Apr-2020

@author: deepa
'''
import os
from datetime import datetime

'''
@param timeStamp: holds the current time whenever called
@param name: holds the name and attribute nomenclature for the sensor 
@param curValue: Holds the current sensor value
@param avgValue: holds the average value for the sensor data 
@param maxValue: holds the max sensor value recorded
@param minValue: holds the min sensor value recorded
@param totvalue: holds the total value to calculate the avgvalue
@param SampleCount: holds the sample count
'''

class SensorData(object):
    
    timeStamp = None
    name = None
    curValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleCount = 0
    pirValue = False
    USLowValueFlag = False
    USRepeatedValueFlag = False
    
    

    
    def __init__(self):
        
        self.timeStamp = str(datetime.now())
        
        
    def addValue(self, newVal):
        '''
        This method updates the sensor data as per the new value
        '''
        self.sampleCount += 1
        self.timeStamp = str(datetime.now())
        self.curValue = newVal
        self.totValue += newVal
        self.totValue = round((self.totValue + newVal),1)
        
        if(self.sampleCount==1):
            self.minValue=self.curValue
        elif(self.curValue < self.minValue):
            self.minValue = self.curValue
        
        if(self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if(self.totValue != 0   and    self.sampleCount > 0):
            self.avgValue = round( (self.totValue / self.sampleCount), 1)
            
    
    def addPIRValue(self, newPIRValue):
        self.timeStamp = str(datetime.now())
        self.sampleCount += 1
        self.pirValue = newPIRValue

    def getUSLowValueFlag(self):
        return self.USLowValueFlag
     
    def setUSLowValueFlag(self, val):
        self.USLowValueFlag = val
        
    def getUSRepeatedValueFlag(self):
        return self.USRepeatedValueFlag
     
    def setUSRepeatedValueFlag(self, val):
        self.USRepeatedValueFlag = val
                
    def getAvgValue(self):
        return self.avgValue
    
    def getMaxValue(self):
        return self.maxValue
    
    def getMinValue(self):
        return self.minValue
    
    def getValue(self):
        return self.curValue
    
    def setName(self, name):
        self.name = name
        
    def getName(self):
        return self.name
        
    def getCount(self):
        return self.sampleCount
        
    '''
    this  method is called to gather the sensor data for further processing for the user/notification
    '''
#     def getSensorData(self):
#         outputStr = \
#         str(self.name + ': ' + \
#             os.linesep + '\tTime:             ' + self.timeStamp + \
# #             os.linesep + '\tPIR:              ' + self.pirValue
#             os.linesep + '\tCurrent Value:    ' + str(self.curValue) + \
#             os.linesep + '\tAverage Value:    ' + str(self.avgValue) + \
#             os.linesep + '\tSamples:          ' + str(self.sampleCount) + \
#             os.linesep + '\tMin:              ' + str(self.minValue) + \
#             os.linesep + '\tMax:              ' + str(self.maxValue))
#         return outputStr
    
