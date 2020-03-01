'''
Created on 23-Feb-2020

@author: deepa
'''
import json
from labs.common.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData

class DataUtil(object):

    #Default Constructor
    def __init__(self):
        '''
        Constructor
        '''
    '''
    Method to Convert SensorData object to Json String
    '''    
    def toJsonFromSensorData(self,sensorData):
        jsonData = json.dumps(sensorData.__dict__)
        
        return jsonData
    
    '''
    Method to Convert Json String to SensorData object
    '''    
    def toSensorDataFromJson(self, jsonData):
        sdDict = json.loads(jsonData)
        sd = SensorData()
        sd.name = sdDict['name']
        sd.timeStamp = sdDict['timeStamp']
        sd.avgValue = sdDict['avgValue']
        sd.minValue = sdDict['minValue']
        sd.maxValue = sdDict['maxValue']
        sd.curValue = sdDict['curValue']
        sd.totValue = sdDict['totValue']
        sd.sampleCount = sdDict['sampleCount']
        
        return sd 
    
    '''
    Method to Convert SensorData object to Json String and write in a file
    '''
    def writeSensorDataToFile(self,sensorData):
        jsonData = json.dumps(sensorData.__dict__)
        
        with open('jsonData_SensorData.txt','w') as outfile:
            json.dump(jsonData, outfile)
            return True
    
    '''
    Method to Convert ActuatorData object to Json String
    '''
    def toJsonFromActuatorData(self,actuatorData):
        jsonData = json.dumps(actuatorData.__dict__)
        
        return jsonData
    
    '''
    Method to Convert Json String to ActuatorData object
    '''
    def toActuatorDataFromJson(self, jsonData):
        adDict = json.loads(jsonData)
        ad = ActuatorData()
        ad.name = adDict['name']
        ad.command = adDict['command']
        ad.val = adDict['val']
        ad.stateData = adDict['stateData']
        ad.timeStamp = adDict['timeStamp']
        
        return ad
    
    '''
    Method to Convert ActuatorData object to Json String and write it in a file
    '''
    def writeActuatorDataToFile(self,actuatorData):
        jsonData = json.dumps(actuatorData.__dict__)
        
        with open('jsonData_ActuatorData.txt','w') as outfile:
            json.dump(jsonData, outfile)
            return True
           
