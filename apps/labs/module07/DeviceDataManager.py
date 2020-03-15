'''
Created on 14-Mar-2020

@author: deepak lokwani

NUID: 001316769
'''

from labs.module07.CoapClientConnector import CoapClientConnector
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
from labs.common.ConfigUtil import ConfigUtil
from labs.common.ConfigConst import ConfigConst

#creating my instance variable for ConfigUtil class
config = ConfigUtil()

#loads my config file
config.loadConfig()

#creating my instance variable for DataUtil class
data = DataUtil()

#getting my ip/domain of the server 
host = config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)

#getting port number to connect
port = int(config.getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))

#defining my resource uri
path = 'Temperature Resource'

#creating my instance variable for SensorData class
sensorData = SensorData()

#adding a new sensordata value
sensorData.addValue(10.00)

#calling the Coapclient connector
coapClient = CoapClientConnector(host, port, path)

#ping request
coapClient.ping()

#get request
coapClient.get()  

#post request
coapClient.post(data.toJsonFromSensorData(sensorData))  

#add new value to sensor data
sensorData.addValue(5.00)

#put request
coapClient.put(data.toJsonFromSensorData(sensorData))  

#delete request
coapClient.delete()  

#stop the Coap client
coapClient.stop()

