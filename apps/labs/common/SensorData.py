'''
Created on 30-Jan-2020

@author: deepak
NUID: 001316769
This class contains the Sensor data to be fetched at the regular intervals
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
    name = 'Sensor Attributes Now'
    curValue = 0
    avgValue = 0
    minValue = 0
    maxValue = 0
    totValue = 0
    sampleCount = 0
    
    humidCountSH = 0
    avgHumidValueSH = 0
    curHumidValueSH = 0
    totHumidValueSH = 0
    
    humidCountI2C = 0
    avgHumidValueI2C = 0
    curHumidValueI2C = 0
    totHumidValueI2C = 0
    
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
        
        if(self.sampleCount==1):
            self.minValue=self.curValue
        elif(self.curValue < self.minValue):
            self.minValue = self.curValue
        
        if(self.curValue > self.maxValue):
            self.maxValue = self.curValue
        if(self.totValue != 0   and    self.sampleCount > 0):
            self.avgValue = self.totValue / self.sampleCount
            
        '''
        Getters and setters are created for f
        '''            
    
    def addHumidityValueSH(self, newHumidValueSH):
        self.humidCountSH += 1
        self.timeStamp = str(datetime.now())
        self.curHumidValueSH = newHumidValueSH
        self.totHumidValueSH += newHumidValueSH
        
        if(self.totHumidValueSH !=0 and self.humidCountSH > 0):
            self.avgHumidValueSH = self.totHumidValueSH / self.humidCountSH
    
    def getHumidityValueSH(self):
        return self.curHumidValueSH
            
    def getAvgHumidValueSH(self):
        return self.avgHumidValueSH
        
    
    def addHumidityValueI2C(self, newHumidValueI2C):
        self.humidCountI2C += 1
        self.timeStamp = str(datetime.now())
        self.curHumidValueI2C = newHumidValueI2C
        self.totHumidValueI2C += newHumidValueI2C
        
        if(self.totHumidValueI2C != 0 and self.humidCountI2C > 0):
            self.avgHumidValueI2c = self.totHumidValueI2C / self.humidCountI2C
            
    def getHumidityValueI2C(self):
        return self.curHumidValueI2C
            
    def getAvgHumidValueI2C(self):
        return self.avgHumidValueI2C
        
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
        
    def getCount(self):
        return self.sampleCount
        
    '''
    this  method is called to gather the sensor data for further processing for the user/notification
    '''
    def getSensorData(self):
        outputStr = \
        str(self.name + ': ' + \
            os.linesep + '\tTime:             ' + self.timeStamp + \
            os.linesep + '\tCurrent Value:    ' + str(self.curValue) + \
            os.linesep + '\tAverage Value:    ' + str(self.avgValue) + \
            os.linesep + '\tSamples:          ' + str(self.sampleCount) + \
            os.linesep + '\tMin:              ' + str(self.minValue) + \
            os.linesep + '\tMax:              ' + str(self.maxValue))
        return outputStr
    
