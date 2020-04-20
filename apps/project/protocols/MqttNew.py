'''
Created on 19-Apr-2020

@author: deepa
'''
import time
import logging
import paho.mqtt.client as mqttClient
import paho.mqtt.publish as publish
from labs.common import DataUtil
from project import MultiActuatorAdaptorTask

class MqttNew(object):
    '''
    Public class that uses the eclipse paho library for Python to import the methods 
    of Mqtt and publish and subscribe the data 
    This class  establishes, subscribes and disconnects the client connection with the 
    channel through a MQTT Broker using Java libraries of Paho. When required the messages 
    in the Message arrived section are directed to the sensordata manager 
    
    '''
    '''
        @param port: the port to which broker is connected
        @param brokerAddr: the domain name of broker
        @param mqttClient: instance variable for MqttClient   
    '''
#     port = None
#     brokerAddr=""
#     brockerKeepAlive = None
#     mqttClient=None
#     data_util = DataUtil.DataUtil()
    
    logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s', level=logging.DEBUG)

    def __init__(self):
        '''
        Default Constructor
        '''
        self.mqttClient = mqttClient.Client("Python_Client2")
        self.brockerKeepAlive = 65
        self.connected_flag = False
        self.port = 1883
        self.brokerAddr = "mqtt.eclipse.org"
        self.act_adap = MultiActuatorAdaptorTask.MultiActuatorAdaptorTask()

    
    def connect(self, connectionCallback = None , msgCallback = None):
        '''
        Function to connect to mqtt broker
        '''
        try:
            #Setting the right callbacks
            if(connectionCallback!=None):
                self.mqttClient.on_connect = connectionCallback
            else:
                self.mqttClient.on_connect = self.onConnect
             
            if(msgCallback !=None) :
                self.mqclient.on_disconnect = msgCallback
            else :
                self.mqttClient.on_disconnect = self.onMessage
             
            #Callback when message arrives
            self.mqttClient.on_message = self.onMessage    
            logging.info("Connecting to broker: "+self.brokerAddr)
         
            #Connect to broker
            self.mqttClient.connect(self.brokerAddr, self.port, self.brockerKeepAlive)
            self.mqttClient.loop_start() 
            while not self.connected_flag:
                logging.info("Attempting to connect to broker: "+self.brokerAddr)
                time.sleep(1)
            return True
        except:
            print("Connection Failed!")
            return False
        
    def disconnect(self):
        '''
        Function to disconnect from broker
        '''
        try:
            logging.info("Disconnecting the MQTT  broker connection ")
            self.mqttClient.disconnect()
            return True
        except:
            print("Disconnecting from broker Failed!!")
            return False
    
        
    def onConnect(self , client ,userData , flags , rc):
        '''
        Callback function when the connection is made with broker
        @param rc: return code for connection  
        '''
        if rc == 0:
            self.connected_flag = True
            logging.info("Connection successful!")
            return True
        else:
            logging.info("Connection Failed, Returned Code: " +rc)
            return False
    
            
    def onMessage(self , client ,userdata , msg):
        '''
        Callback function when message arrives
        '''
        try:
#         print("NEW")
#         print(msg)
            topic = str(msg.topic)
            data = str(msg.payload.decode("utf-8"))
            print("")
            print("Received Actuation : " + topic)
            print("Actuation Value: " + data)
            self.act_adap.updateActuator("ActFromGD", data)
#             self.act_adap.updateActuator(topic,data)
            return True
        except:
            print("Displaying Message Failed!!")
            return False

            
    def publishMessage(self , topic , msg , qos=2):
        '''
        Function to publish message
        @param topic: name of the topic to publish message
        @param msg: The message to be sent   
        '''
        try:
#             print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
            logging.info("Publishing:" + msg)
            self.mqttClient.publish(topic, msg, qos)
            return True
        except:
            print("Publishing Message Failed!!")
            return False

    #Method to publish the Message on Topic  using Mqtt    
    def publish_message(self,sensor_data,topic):
        logging.info("Converting SensorData to Json and Publishing......")
        jsonData = self.data_util.toJsonFromSensorData(sensor_data)
        #self.client.loop_start()
        try:
            publish.single(topic,jsonData, hostname="mqtt.eclipse.org")
            #publish.single(topic,jsonData, 2)
            print("Publishing Successful!")
            return True
        except:
            print("Publishing Failed!!")
            return False
        logging.info("JsonData: "+jsonData)  
    
    def subscibetoTopic(self , topic ,connnectionCallback = None, qos=2):
        '''
        Function to subscribe to a topic
        @param topic: name of the topic to subscribe to 
        @param connectionCallback:    
        '''
        try:
            if connnectionCallback != None:
                self.mqttClient.on_subscribe = (connnectionCallback)
                self.mqttClient.on_message = (connnectionCallback)
            
            self.mqttClient.subscribe(topic , qos)
            print("Subscribed to: " + topic)
            return True
        except:
            print("Subscribing to topic Failed!!")
            return False
        
        
    
        
    def unsubscibefromTopic(self , topic):
        '''
        Function to unsubscribe to a topic
        
        '''       
        logging.info("Unsubscribing from topic: "+topic)
        self.mqttClient.unsubscribe(topic)
    
