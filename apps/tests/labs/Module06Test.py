import unittest
from labs.module06 import MQTTClientConnector
from labs.common import SensorData


"""
Test class for all requisite Module06 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module06Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.mqttClientConnector = MQTTClientConnector.MQTTCLientConnector()
		self.sensorData 		 = SensorData.SensorData()
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.mqttClientConnector = None
		self.sensorData 		 = None
		pass

	"""
	This test case checks the functioning of the On_Connect callback function of the MQTT 
	"""
	def testOn_Connect(self):
		y = self.mqttClientConnector.on_connect("DeviceClient", self.sensorData, 1, 0)
		z = self.mqttClientConnector.on_connect("DeviceClient", self.sensorData, 1, 1)
		assert(y == True)
		assert(z == False)
	
	"""
	This test case checks the functioning of the PublishMessage callback function of the MQTT 
	"""	
	def testPublishMessage(self):
		y = self.mqttClientConnector.publishMeassage(self.sensorData)
		assert(y)
	"""
	This test case checks the functioning of the OnDisconnect callback function of the MQTT 
	"""	
	def testOnDisconnect(self):
		y = self.mqttClientConnector.on_disconnect("DeviceClient", self.sensorData, 0)
		assert(y)
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()