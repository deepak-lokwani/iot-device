'''
Created on 14-Mar-2020

@author: deepak lokwani

NUID: 001316769
'''

from coapthon.client.helperclient import HelperClient

'''
This class creates a python based CoAp client connector using capthon library
This class connects to the server using its host, port and the path
This class defines all the methods (ping, PUT, DELETE, GET, POST) for the COAP protocol
'''

class CoapClientConnector(object):
    '''
    connects to the CoAP server
    Initial Constructor
    '''
    def __init__(self, host, port, path):
        '''
        constructor
        @param host: ip/domain of the server
        @param port: port number to connect 
        @param path: resource uri  
        '''
        self.host = host
        self.port = port
        self.path = path
        self.client = HelperClient(server=(host, port))
    
    def ping(self):
        '''
        function to ping my CoAp server
        It returns a true boolean flag when successful
        '''    
        try:
            self.client.send_empty("")
            return True
        except:
            return False
        
    def get(self):
        '''
        my function to GET CoAp resource request
        It returns a true boolean flag when successful
        '''
        try:
            response = self.client.get(self.path)
            print(response.pretty_print())
            return True
        except:
            return False
        
    def post(self, jsonData):
        '''
        my function to POST request
        It takes a Json string of the  SensorData object as a parameter for the POST function
        It returns a true boolean flag when successful
        @param jsonData: message/data to POST
        '''
        try:
            response = self.client.post(self.path, jsonData)
            print(response.pretty_print())
            return True
        except:
            return False
    
    def put(self, jsonData):
        '''
        my Wrapper method for the PUT action
        It takes a Json string of the  SensorData object as a parameter for the PUT function
        It returns a true boolean flag when successful
        @param jsonData: meassge or data to PUT 
        '''
        try:
            response = self.client.put(self.path, jsonData)
            print(response.pretty_print())
            return True
        except:
            return False
        
    def delete(self):
        '''
        my function to DELETE the CoAp resource request
        It returns a true boolean flag when successful
        ''' 
        try:
            response = self.client.delete(self.path)
            print(response.pretty_print())
            return True
        except:
            return False        
        
        
    def stop(self):
        '''
        my function to stop the CoAp client connection
        '''  
        self.client.stop()     