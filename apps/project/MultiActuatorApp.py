'''
Created on 18-Apr-2020

@author: deepa
'''
from time import sleep
import threading
# from labs.module08 import MqttClientConnector
# from project.commons import MqttClientConnector
from project.protocols import MqttNew

class MultiActuatorApp(threading.Thread):
    
    '''
    This class is used to start the thread for subscribing topic of Mqtt broker
    '''
    
    #Default Constructor
    def __init__(self):
        super(MultiActuatorApp,self).__init__()

    #Run method for getting the values
    def run(self):
        while True:
            #MqttClientConnector instance
#             self.mqttClient = MqttClientConnector.MqttClientConnector()
            self.mqttClient = MqttNew.MqttNew()
        
            #Connecting to broker
            self.mqttClient.connect(None, None)

            #Subscribing to a topic
            self.mqttClient.subscibetoTopic("ActFromGD")

            sleep(300)

            #Unsubscribe from topic
#             self.mqttClient.unsubscibefromTopic("ActFromGD")

            #Disconnecting from broker
#             self.mqttClient.disconnect()