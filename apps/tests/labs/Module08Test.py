import unittest
from labs.module08 import MqttClientConnector
from time import sleep


"""
Test class for all requisite Module08 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
class Module08Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	def setUp(self):
		self.connector = MqttClientConnector.MqttClientConnector()

	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.connector = None

	"""
	Place your comments describing the test here.
	"""
	def testMqttSubscribe(self):
		
		i=10
		while(i!=0):
			self.connector.connect(None, None)
			sleep(1)
			self.connector.subscibetoTopic("Mqtt_Test")
			sleep(15)
			self.connector.unsubscibefromTopic("Mqtt_Test")
			self.connector.disconnect()
			i=i-1
		
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()