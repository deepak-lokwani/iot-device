import unittest


"""
Test class for all requisite DataUtil functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.common.SensorData import SensorData
from labs.common.DataUtil import DataUtil
import json
from labs.common.ActuatorData import ActuatorData
class DataUtilTest(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.sensor_Data = SensorData() 
		self.actuator_Data = ActuatorData()
		self.dataUtil = DataUtil
		pass

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.sensor_Data = None
		self.dataUtil = None
		pass
	
	"""
	Place your comments describing the test here.
	"""
	def testToJsonFromSensorData(self):
		self.sensorData = SensorData()
		jsonData = json.dumps(self.sensorData.__dict__)
		json_data = self.dataUtil.toJsonFromSensorData(self, self.sensor_Data) 
		assert(json_data == jsonData)
		

	def testToJsonFromActuatorData(self):
		self.actData = ActuatorData()
		jsonData = json.dumps(self.actData.__dict__)
		json_Data = self.dataUtil.toJsonFromActuatorData(self, self.actuator_Data)
		assert(json_Data == jsonData)
		
	def testWriteSensorDataToFile(self):
# 		js = json.dumps(self.sensor_Data)
		y = self.dataUtil.writeSensorDataToFile(self, self.sensor_Data)
		assert(y)
		
	def testWriteActuatorDataToFile(self):
		y = self.dataUtil.writeActuatorDataToFile(self, self.actuator_Data)
		assert(y)

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()