'''
Created on 15-Feb-2020

@author: deepak_lokwani
'''

'''
this class is responsible for fetching the Humidity data from the SenseHat Sensor directly through the I2C protocol
'''
import smbus
import threading
from time import sleep
import logging
from labs.common import ConfigUtil
from labs.common import ConfigConst
from labs.common import SensorData
from labs.module05 import SensorDataManager

i2cBus = smbus.SMBus(1) # Use I2C bus No.1 on Raspberry Pi 3+

enableControl = 0x2D
enableMeasure = 0x08
accelAddr = 0x1C # address for IMU (accelerometer)
magAddr = 0x6A 	 # address for IMU (magnetometer)
pressAddr = 0x5C # address for pressure sensor
humidAddr = 0x5F # address for humidity sensor
begAddrL = 0x28	 # address for the Least byte of the relative Humidity
begAddrM = 0x29  # address for the Most byte of the relative Humidity
totBytes = 6
DEFAULT_RATE_IN_SEC = 10	#Sleep Time

class I2CSenseHatAdaptor(threading.Thread):
	rateInSec = DEFAULT_RATE_IN_SEC
	sensorData = SensorData.SensorData()
	sensorDataMgr = SensorDataManager.SensorDataManager()
	humidityInPercent = 0

	'''
	Initializing my constructor and I2CBus consequently
	'''
	def __init__(self):
		super(I2CSenseHatAdaptor, self).__init__()
		self.initI2CBus()
		self.enableEmulator = False
	'''
	enabling the Emulator
	'''	
	def setEmulator(self, boolean):
		self.enableEmulator = boolean
	
	'''
	Initializing my I2CBus
	'''	
	def initI2CBus(self):
		logging.info("Initializing I2C bus and enabling I2C addresses...")
		i2cBus.write_byte_data(humidAddr, enableControl, enableMeasure)
	
	'''
	method to convert my signed data to the unsigned data
	'''	
	def signedToUnsigned(self,lsb,msb):
		val = (msb << 8) | lsb
		if val & (1 << 15):
			val = val - (1 << 16)
		return val
	'''
    method to get my humidity data through the I2C bus
    '''
	def getHumidityDataI2C(self):
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
		self.humidityInPercent=(relativeHumidity/(valH1T0 - valH0T0)) + h0_rh
		datax = i2cBus.read_i2c_block_data(humidAddr, begAddrL, totBytes)
		datay = i2cBus.read_i2c_block_data(humidAddr, begAddrM, totBytes)
	
	'''
	method to update my humidity  data  through the SensorData instance
	'''	
	def updateHumidityValueI2C(self):
		self.sensorData.addHumidityValueI2C(self.humidityInPercent)
	
	'''
	method to display my humidity data
	'''	
	def displayHumidityDataI2C(self):	
		print("Relative Humidity through I2C:  %.2f" %self.humidityInPercent)
	
	'''
	Thread starts here
	'''
	def run(self):
		while True:
			if self.enableEmulator:
				self.getHumidityDataI2C()
				self.updateHumidityValueI2C()
				self.displayHumidityDataI2C()
				self.sensorDataMgr.handleSensorData(self.sensorData.getHumidityValueI2C(), 'humidI2C')	
			sleep(self.rateInSec)
