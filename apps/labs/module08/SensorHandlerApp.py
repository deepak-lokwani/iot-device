'''
Created on 23-Mar-2020

@author: deepak lokwani

'''

'''
This class establishes, subscribes, unsubscribes, and disconnects 
the connection with the Gateway device infinitely while the program 
is running in order to continuously receive the Actuation data values back.

'''
from labs.module08 import MqttClientConnector
from time import sleep

while(True):
        
    
    #MqttClientConnector instance
    connector = MqttClientConnector.MqttClientConnector()
    
    #Connecting to broker
    connector.connect(None, None)
    connector.publishMessage("Mqtt_Test", "msg", 2)
    
    #subscribing to a topic
    connector.subscibetoTopic("Mqtt_Test")
    
    #pause
    sleep(65)
     
    #unsubscribe from topic
    connector.unsubscibefromTopic("Mqtt_Test")
     
    #disconnecting from broker
    connector.disconnect()