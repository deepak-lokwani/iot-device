import unittest
from project import MultiActuatorAdaptorTask
from project.commons import MqttClientConnector
from project import SystemPerformanceAdaptor
from project.protocols import UbidotsApiConnector
from project.commons.SensorData import SensorData
from labs.common.ActuatorData import ActuatorData 
from labs.common.DataUtil import DataUtil

"""
Test class for all requisite Project functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class ProjectTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.multi_act_apt = MultiActuatorAdaptorTask.MultiActuatorAdaptorTask()
		self.mqtt = MqttClientConnector.MqttClientConnector()
		self.ubi = UbidotsApiConnector
		self.sensorData = SensorData()
		self.actuatorData = ActuatorData()
# 		self.actData = ActuatorData()
		self.dataUtil = DataUtil
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.multi_act_apt = None
		self.mqtt = None
		self.sp = None
		self.ubi = None
		self.sensorData = None
		self.actuatorData = None
		self.dataUtil = None
		pass

	"""
	Place your comments describing the test here.
	"""
	def testMultiActuatorAdaptor(self):
		self.returnBooleanVal = self.multi_act_apt.updateActuator('ActFromGD', "0")
		assert(self.returnBooleanVal)
		self.returnBooleanVal2 = self.multi_act_apt.updateActuator('ActFromGD',"1")
		assert(self.returnBooleanVal2)
		
	def testMqttconnect(self):
		assert(self.mqtt.connect(None, None))
		
	def testMqttsubscribetoTopic(self):
		assert(self.mqtt.subscibetoTopic('ActFromGD'))
		
	def testMQttdisconnect(self):
		assert(self.mqtt.disconnect())	
		
	def testUbidotsApiConnector(self):
		cpuUtil = 50.0
		memUtil = 75.0
		assert(self.ubi.main(cpuUtil, memUtil))
		
		

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()