'''
Created on 30-Jan-2020

@author: deepak
NUID: 001316769
This class loads the configuration file for the SMTP Client

'''
import configparser
from labs.common import ConfigConst
import os

class ConfigUtil(object):
    '''
    classdocs
    '''
    configData  =   None
    isLoaded    =   False
    configConst =   None
    
    def __init__(self):
        '''
        Constructor
        '''
        '''
        Creates instances of  ConfigConst, ConfigParser and calls the loadConfig function
        '''
        self.configConst    =   ConfigConst.ConfigConst()
        self.configData     =   configparser.ConfigParser()
        self.configFilePath =   self.configConst.DEFAULT_CONFIG_FILE_NAME
        self.loadConfig()
        
    def loadConfig(self):
        '''
        Method to load the ConfigUtil file with the props file/ConfigConst file
        '''
        if(os.path.exists(self.configFilePath)):
            self.configData.read(self.configFilePath)
            self.isLoaded   =   True
        else:
            path=self.configFilePath
            os.mkdir(path) 
            self.configData.read(self.path)
            self.isLoaded   =   True
            
    def getConfigFile(self):
        #creating getter for the ConfigFile
        return self.configFilePath
    
    def getProperty(self, section, key):
        #Creating GetProperty for the Configutil
        self.loadConfig()
        return self.configData.get(section,key)
    
    def hasConfigData(self):
        #check if the configuration is loaded or not
        return self.isLoaded
    
    def hasProperty(self, propname):
        #checks if the property is assigned or not, created for the Test case
        if(self.getProperty("smtp.cloud", propname)):
            return True
        else:
            return False
    #function checks for sections
    def hasSection(self, sectionname):
        #checks if the Section is assigned or not, created for the Test case
        if(self.configData.has_section(sectionname)):
            return True
        else:
            return False