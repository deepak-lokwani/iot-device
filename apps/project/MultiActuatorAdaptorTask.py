'''
Created on 19-Apr-2020

@author: deepa
'''
from labs.common.ActuatorData import ActuatorData as ActData, CMD_ON
from labs.common.DataUtil import DataUtil
import logging

class MultiActuatorAdaptorTask(object):
    
    def __init__(self):
        self.ActData = ActData()
        self.dUtil = DataUtil()
        
    #Method for checking ActutatorData initialization
    def updateActuator(self, act_type, data):
        
        if act_type == "ActFromGD" :
            
            if(data == "1"):
                self.stateVal = "ON"
            elif(data == "0"):
                self.stateVal = "OFF"
                
            self.ActData.setName("LED ACTUATOR")
            self.ActData.setCommand(data)
            self.ActData.setValue(data)    
            self.ActData.setStateData(self.stateVal)
            self.ActData.updateData(self.ActData)
            print("Actuator Name: " + self.ActData.getName())
#             print("COMMAND: " + self.ActData.getCommand())
            jsonData = self.dUtil.toJsonFromActuatorData(self.ActData)
            logging.info("Actuator JSON: " + jsonData)
            return True
        else:
            print("Failed to send Actuation Signal")
            return False