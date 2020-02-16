'''
Created on 08-Feb-2020

@author: deepak
'''
'''
this python script starts the entire Temperature Hnadling process here. This is the main/start process
'''

from labs.module03 import TempSensorAdaptorTask
import sys
sys.path.insert(0,'/home/pi/workspace/iot-device/connected-devices-python/apps')
# print(sys.path)


# instance of temperature Emulator created with threshold value
alert_diff = 0.05
simulator = TempSensorAdaptorTask.TempSensorAdaptorTask(alert_diff)
# enabled the emulator
simulator.setEmulator(True)
#thread starting
simulator.start()
