'''
Created on 23-Mar-2020

@author: deepa
'''
from labs.module08 import MqttClientConnector
from time import sleep

while(True):
        
    
    #MqttClientConnector instance
    connector = MqttClientConnector.MqttClientConnector()
    
    #Connecting to broker
    connector.connect(None, None)
    
    #subscribing to a topic
    connector.subscibetoTopic("Mqtt_Test")
    
#     #pause
    sleep(65)
#     
    #unsubscribe from topic
    connector.unsubscibefromTopic("MqttTTest")
     
    #disconnecting from broker
    connector.disconnect()