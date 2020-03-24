'''
Created on 23-Mar-2020

@author: deepa
'''

import time
import paho.mqtt.client as mqttClient
from labs.common import ConfigUtil
from labs.common import SensorData
from labs.common import DataUtil
import ssl


class MqttClientConnector(object):
    '''
    mqtt connector
    Functions to connect to broker, subscribe message , publish message
    disconnect from broker 
    @param port: the port to which broker is connected
    @param brokerAddr: the domain name of broker
    @param mqttClient: instance variable for MqttClient
    @param config: instance variable for ConfigUtil class   
    '''
    port = None
    brokerAddr=""
    brockerKeepAlive = None
    mqttClient=None
    config = None
    

    def __init__(self):
        '''
        Constructor
        '''
        self.mqttClient = mqttClient.Client("Python_Client")
        self.config = ConfigUtil.ConfigUtil()
        self.sensoData = SensorData.SensorData()
        self.datautil = DataUtil.DataUtil()
        self.config.loadConfig()
        self.brockerKeepAlive = 65
        self.connected_flag = False
        self.pemfile = 'C:\\Users\\deepa\\git\\workspace\\ubidots_cert.pem'
        self.authToken = 'BBFF-yegKC0ObS7wjfGO8Bx2IU53hjRv9il'
        self.port = 1883
        self.brokerAddr = 'mqtt.eclipse.org'
        self.password = ''
    
    def connect(self, connectionCallback = None , msgCallback = None):
        '''
        Function to connect to mqtt broker
        '''
        #Setting the right callbacks
        if(connectionCallback!=None):
            self.mqttClient.on_connect = connectionCallback
        else:
            self.mqttClient.on_connect = self.onConnect
            
        if(msgCallback !=None) :
            self.mqclient.on_disconnect = msgCallback
        else :
            self.mqttClient.on_disconnect = self.onMessage
        #callback when message arrives
        self.mqttClient.on_message = self.onMessage    
        print("Connecting to broker",self.brokerAddr)
        self.mqttClient.connect(self.brokerAddr, self.port, self.brockerKeepAlive)
        self.mqttClient.loop_start() 
        while not self.connected_flag:
            print("Attempting to connect to MQTT broker :",self.brokerAddr)
            time.sleep(1)
        
    def disconnect(self):
        '''
        function to disconnect from broker
        '''
        print("Disconneting the MQTT  broker connection ")
        self.mqttClient.disconnect()
    
        
    def onConnect(self , client ,userData , flags , rc):
        '''
        callback when the connection is made with broker
        @param rc: return code for connection  
        '''
        if rc == 0:
            self.connected_flag = True
            print("Connected OK returned Code:" , rc)
        else:
            print("Bad connection Returned Code:", rc)
    
            
    def onMessage(self , client ,userdata , msg):
        '''
        callback when message arrives
        '''
        print("Recieved Message from Gateway: " + str(msg.payload.decode("utf-8")))
       
       
            
    def publishMessage(self , topic , msg , qos=2):
        '''
        function to publish message
        @param topic: name of the topic to publish message
        @param msg: The message to be sent   
        '''
        print("Publishing:",msg)
        self.mqttClient.publish(topic, msg, qos)
    
    
    def subscibetoTopic(self , topic ,connnectionCallback = None, qos=2):
        '''
        function to subscribe to a topic
        @param topic: name of the topic to subscribe to 
        @param connectionCallback:   
        '''
        if connnectionCallback != None:
            self.mqttClient.on_subscribe = (connnectionCallback)
            self.mqttClient.on_message = (connnectionCallback)
        self.mqttClient.subscribe(topic , qos)
        
    
        
    def unsubscibefromTopic(self , topic):
        '''
        function to unsubscribe to a topic
        '''       
        print("Unsubscribing from topic",topic)
        self.mqttClient.unsubscribe(topic)
    