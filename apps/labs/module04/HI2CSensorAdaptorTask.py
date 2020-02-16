'''
Created on 15-Feb-2020

@author: deepak
'''

import smbus
import threading
from time import sleep
import logging
from labs.common import ConfigUtil
from labs.common import ConfigConst

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi 3+

enableControl = 0x2D
enableMeasure = 0x08
accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor
begAddrL = 0x28
begAddrM = 0x29
totBytes = 6
DEFAULT_RATE_IN_SEC = 10

class I2CSenseHatAdaptor(threading.Thread):
	rateInSec = DEFAULT_RATE_IN_SEC
	#config = ConfigUtil.ConfigUtil()
	


	def __init__(self):
		super(I2CSenseHatAdaptor, self).__init__()
		#self.config = ConfigUtil.ConfigUtil(ConfigConst.DEFAULT_CONFIG_FILE_NAME)
		#self.config.loadConfig()
		#print('Configuration data...\n' + str(self.config))
		self.initI2CBus()
		self.enableEmulator = False
		
	def setEmulator(self, boolean):
		self.enableEmulator = boolean
		
	def initI2CBus(self):
		logging.info("Initializing I2C bus and enabling I2C addresses...")
		#i2cBus.write_byte_data(accelAddr, enableControl, enableMeasure)
		#i2cBus.write_byte_data(magAddr, enableControl, enableMeasure)
		#i2cBus.write_byte_data(pressAddr, enableControl, enableMeasure)
		i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)
		
	def signedToUnsigned(self,lsb,msb):
		val = (msb << 8) | lsb
		if val & (1 << 15):
			val = val - (1 << 16)
		return val
    
	def displayHumidityData(self):
		bits = 8
		
		coeffH0 = i2cBus.read_byte_data(humidAddr, 0x30)
		coeffH1 = i2cBus.read_byte_data(humidAddr, 0x31)
		h0_rh = coeffH0 >> 1
		h1_rh = coeffH1 >> 1
		
		valH0T0a = i2cBus.read_byte_data(humidAddr, 0x36)
		valH0T0b = i2cBus.read_byte_data(humidAddr, 0x37)
		valH0T0 = self.signedToUnsigned(valH0T0a,valH0T0b)
		
		valH1T0a = i2cBus.read_byte_data(humidAddr, 0x3A)
		valH1T0b = i2cBus.read_byte_data(humidAddr, 0x3B)
		valH1T0 = self.signedToUnsigned(valH1T0a,valH1T0b)
		
		data_1 = i2cBus.read_byte_data(humidAddr, begAddrL)
		data_2 = i2cBus.read_byte_data(humidAddr, begAddrM)
		data = self.signedToUnsigned(data_1,data_2)
		
		relativeHumidity = (data - valH0T0)*(h1_rh - h0_rh)
		humidityInPercent=(relativeHumidity/(valH1T0 - valH0T0)) + h0_rh
		datax = i2cBus.read_i2c_block_data(humidAddr, begAddrL, totBytes)
		datay = i2cBus.read_i2c_block_data(humidAddr, begAddrM, totBytes)
		print("Relative Humidity through I2C:  %.2f" %humidityInPercent)
	
	def run(self):
		while True:
			if self.enableEmulator:
				self.displayHumidityData()	
			sleep(self.rateInSec)
