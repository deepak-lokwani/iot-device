'''
Created on 15-Feb-2020

@author: deepak_lokwani
'''

'''
this class is responsible for fetching the Humidity data from the SenseHat Sensor directly through the SENSE_HAT API
'''

import threading
from time import sleep
import logging
from labs.common import ConfigUtil
from labs.common import ConfigConst
from sense_hat import SenseHat
from labs.common import SensorData
from labs.module04 import SensorDataManager
DEFAULT_RATE_IN_SEC = 10   #sleep time

class HumiditySensorAdaptorTask(threading.Thread):
	'''
	creating the required instances
	'''
	rateInSec = DEFAULT_RATE_IN_SEC
	config = ConfigUtil.ConfigUtil()
	sensorData = SensorData.SensorData()
	sensorDataMgr = SensorDataManager.SensorDataManager()
	
	def __init__(self):
		'''
		Initializing my constructor and SenseHAT API consequently
		'''
		threading.Thread.__init__(self)
		self.enableEmulator = False
		self.senseHat = SenseHat()
		self.initHumidity()
		self.humidityData = self.senseHat.get_humidity()
		

	def initHumidity(self):
		logging.info("Fetching data from SenseHat API...")
		
	'''
	enabling the Emulator
	'''		
	def setEmulator(self, boolean):
		self.enableEmulator = boolean
		
	'''
	method to display my humidity data
	'''		
	def displayHumidityData(self):
		print('Relative Humidity through SenseHat data:   ' + str(self.humidityData))
	
	'''
	method to update my humidity  data  through the SensorData instance
	'''	
	def updateHumidityValueSH(self):
		self.sensorData.addHumidityValueSH(self.humidityData)
	
	'''
	Thread starts here
	'''			
	def run(self):
		while True:
			if self.enableEmulator:
				self.updateHumidityValueSH()
				self.displayHumidityData()
				self.sensorDataMgr.handleSensorData(self.sensorData.getHumidityValueSH(), 'humidSH')
				
			sleep(self.rateInSec)
				
				
