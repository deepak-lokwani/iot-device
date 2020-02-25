'''
Created on 23-Feb-2020

@author: deepa
'''
from labs.common.DataUtil import DataUtil
from labs.common.ActuatorData import ActuatorData
from labs.common.ActuatorDataListener import  ActuatorDataListener
from labs.common.SensorDataListener import SensorDataListener
import redis


class PersistenceUtil(object):
    
    #Default Constructor
    def __init__(self):
        self.dataUtil = DataUtil()
        self.redis_connection = redis.Redis(host='localhost', port=6379)
        self.actuatorDataListener  = ActuatorDataListener()
        self.sensorDataListener    = SensorDataListener()
        
    '''
    Write the actutorData to the DBMS 
    '''    
    def readActuatorDataToDbms(self):
        redis_subscribe = self.redis_connection().pubsub()
        actuatorData_subscribe = redis_subscribe.subscribe("ActuatorData")
        redis_message = redis_subscribe.getMessage()
        self.registerActuatorDatatoDbmsListener()
        return 
    
    ''' Method to write SensorData to DBMS''' 
    def writeSensorDataToDbms(self,sensorData):
        json_sensorData = self.dataUtil.toJsonFromSensorData(sensorData)
        self.redis_connection.pubsub()
        self.redis_connection.publish("SensorData", json_sensorData)
        self.registerSensorDataToDbmsListener()
        return 
    
    def registerSensorDataToDbmsListener(self):
        self.sensorDataListener.OnMessage()
        
    def registerActuatorDataToDbmsListener(self):
        self.actuatorDataListener.OnMessage()    
