'''
Created on 15-Feb-2020

@author: deepak
'''

import threading
from time import sleep
import logging
from labs.common import ConfigUtil
from labs.common import ConfigConst
from sense_hat import SenseHat
DEFAULT_RATE_IN_SEC = 10

class HumiditySensorAdaptorTask(threading.Thread):
	rateInSec = DEFAULT_RATE_IN_SEC
	config = ConfigUtil.ConfigUtil()
	
	
	def __init__(self):
		threading.Thread.__init__(self)
		self.enableEmulator = False
		#self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
		#self.config.loadConfig()
		self.senseHat = SenseHat()
		self.initHumidity()
		

	def initHumidity(self):
		logging.info("Fetching data from SenseHat API...")
		
	def setEmulator(self, boolean):
		self.enableEmulator = boolean
		
	def displayHumidityData(self):
		self.humidityData = self.senseHat.get_humidity()
		print('Relative Humidity through SenseHat data:   ' + str(self.humidityData))
				
	def run(self):
		while True:
			if self.enableEmulator:
				self.displayHumidityData()
				
			sleep(self.rateInSec)
				
				
