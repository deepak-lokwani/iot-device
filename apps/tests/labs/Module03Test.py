import unittest
from labs.module03 import SensorDataManager 
from labs.module03 import TempSensorAdaptorTask
from labs.common import SensorData

"""
Test class for all requisite Module03 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module03Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.tempAdaptor	 = TempSensorAdaptorTask.TempSensorAdaptorTask(2)
		self.sensDataMan = SensorDataManager.SensorDataManager()
		self.currentValue = self.tempAdaptor.sensorData.getValue()
		self.s = SensorData.SensorData().getValue()
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.tempAdaptor = None
		self.currentValue = None
		self.sensDataMan = None
		


	"""
	Unit Test method for TempAdaptorTask class
	"""
	def testTempSensorAdaptorTask(self):
		
		self.assertTrue(isinstance(self.currentValue, int), "CurrentValue in Sensor Data Value is not Float")  #Checking if the value is not float	
		pass
	
	
	"""
	Unit Test for SensorDataManager class
	"""
	def testSensorDataManager(self):
		self.assertFalse(self.sensDataMan.handleSensorData(self.s),"SesnorDataManager Failed")
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()