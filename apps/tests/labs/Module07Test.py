import unittest
"""
Test class for all requisite Module07 functionality.

Instructions:
1) Rename 'testSomething()' method such that 'Something' is specific to your needs; add others as needed, beginning each method with 'test...()'.
2) Add the '@Test' annotation to each new 'test...()' method you add.
3) Import the relevant modules and classes to support your tests.
4) Run this class as unit test app.
5) Include a screen shot of the report when you submit your assignment.

Please note: While some example test cases may be provided, you must write your own for the class.
"""
from labs.module07.CoapClientConnector import CoapClientConnector
from labs.common.ConfigUtil import ConfigUtil
from labs.common.ConfigConst import ConfigConst

class Module07Test(unittest.TestCase):

	"""
	Use this to setup your tests. This is where you may want to load configuration
	information (if needed), initialize class-scoped variables, create class-scoped
	instances of complex objects, initialize any requisite connections, etc.
	"""
	
	
	def setUp(self):
		
		#getting the host data
		host = ConfigUtil().getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.HOST_KEY)
		
		#port number to connect
		port = int(ConfigUtil().getProperty(ConfigConst.COAP_DEVICE_SECTION, ConfigConst.PORT_KEY))
		
		#resource uri
		path = 'Temperature Resource'
		
		#connecting to my CoAp client connector
		self.coap_client = CoapClientConnector(host,port,path)
	
	
	"""
	Use this to tear down any allocated resources after your tests are complete. This
	is where you may want to release connections, zero out any long-term data, etc.
	"""
	def tearDown(self):
		self.coap_client = None

	
	"""
	Unit Test Method to check my ping functionality
	"""
	def test_ping(self):
		assert(self.coap_client.ping())
	
		
	"""
	Unit Test Method to check my GET functionality
	"""
	def test_get(self):
		assert(self.coap_client.get())
	
	"""
	Unit Test Method to check my PUT functionality
	"""
	def test_put(self):
		jsonData="{'name': 'temperature'}" 
		assert(self.coap_client.put(jsonData))
	
	"""
	Unit Test Method to check my POST functionality
	"""
	def test_post(self):
		jsonData="{'name': 'temperature'}" 
		assert(self.coap_client.post(jsonData))
	
	"""
	Unit Test Method to check my DELETE functionality
	"""
	def test_delete(self): 
		assert(self.coap_client.delete())
		
			
if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()
