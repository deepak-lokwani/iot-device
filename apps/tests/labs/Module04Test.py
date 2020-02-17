import unittest
from labs.module04 import MultiActuatorAdaptor
from labs.module04 import SensorDataManager
from labs.common import SensorData

"""
Test class for all requisite Module04 functionality.

Instructions:

1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""

class Module04Test(unittest.TestCase):
	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.tesFunction = MultiActuatorAdaptor.TempActuatorAdaptor()
		self.tesFunction2 = SensorDataManager.SensorDataManager()
		self.tesVariable = SensorData.SensorData().getHumidityValueSH()
	
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""

	def tearDown(self):
		self.tesFunction = None

	"""
	this class confirms the integrity of the MultiActuatorAdaptor Class bu returning a boolean value.
	"""
	def testMultiActuatorAdaptor(self):
		self.returnBooleanVal = self.tesFunction.updateActuator(20.00, 'humidSH')
		assert(self.returnBooleanVal)
		self.returnBooleanVal2 = self.tesFunction.updateActuator(20.00, 'humidI2C')
		assert(self.returnBooleanVal2)

	'''
	this class confirms the integrity of the SensorDataManager class by sending a test variable(through SensorData instance) 
	and checks if the ActuatorAdaptor instance is created or not
	this class returns None (Null) when failed 
	'''
	def testSensorDataManager(self):
		self.tesFunction2.handleSensorData(self.tesVariable, 'humidSH')

if __name__ == "__main__":
	# import sys;sys.argv = ['', 'Test.testName']
	unittest.main()

