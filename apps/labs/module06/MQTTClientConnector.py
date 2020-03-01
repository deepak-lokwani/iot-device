'''
Created on 29-Feb-2020

@author: deepak
'''

'''
this class establishes, publishes and disconnects the client connection with the channel through a MQTT Broker using Python libraries of Paho
'''
import paho.mqtt.client as mqtt
from labs.common import SensorData
from labs.common import ActuatorData
from labs.common import ConfigUtil
from labs.common import DataUtil
import time
import logging
from paho.mqtt.publish import _on_connect

class MQTTCLientConnector(object):
    '''
    this class establishes, publishes and disconnects the client connection with the channel through a MQTT Broker using Python libraries of Paho
    '''
    def __init__(self):
        '''
        this is a default constructor 
        '''
        #Initializing my variables and the instances
        self.dataUtil = DataUtil.DataUtil()
        self.sensorData = SensorData.SensorData()
        self.actuatorData = ActuatorData.ActuatorData()
        
        self.mqttBrokerAddr = 'mqtt.eclipse.org' 
        self.port = 1883
        self.keepAlive = 65
        self.connectedFlag = False
        self.topic = "Raspi/Temperature"
        self.mqttClient = mqtt.Client("DeviceClient")
        self.mqttClient.on_connect = self.on_connect
        self.mqttClient.on_disconnect = self.on_disconnect
        self.mqttClient.connect(self.mqttBrokerAddr, self.port, self.keepAlive)
        
        
    def on_connect(self, client, userdata, flags, rc):
        '''
        Callback function when the connection is made with the broker
        '''
        self.mqttClient.on_message = self.on_Message
        if rc == 0:
            self.connectedFlag = True
            logging.info("OK Connection successful, Returned Code: "  + str(rc))
            return True
        else:
            logging.info("Bad Connection, Returned Code: " + str(rc))
            return False
        
            
    def publishMeassage(self, sensorData):
        '''
        this method publishes the message as and when it is triggered
        '''
        jsonSensorData = DataUtil.DataUtil().toJsonFromSensorData(sensorData)
        self.mqttClient.loop_start()
        logging.info("Publishing: " + jsonSensorData)
        self.mqttClient.publish(self.topic, jsonSensorData, 1)
        self.mqttClient.publish(self.topic, jsonSensorData , 2)
        return True
        
        
    def on_Message(self, client, userdata, msg):
        '''
        my method to get a callback whenever a message arrives
        '''
        logging.info("Topic: " + str(msg.topic))
        logging.info("QOS: " + str(msg.qos))
        logging.info("Retain flag: " + msg.retain)
        return True
        
    def on_disconnect(self, client, userdata, rc):
        logging.info("Disconnecting the MQTT Broker with return code: " + str(rc))
        #self.mqttClient.loop_stop()
        self.mqttClient.disconnect(rc)
        return True

        
        
        