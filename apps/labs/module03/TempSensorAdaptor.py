'''
Created on 08-Feb-2020

@author: deepak
'''
from labs.module03 import TempSensorAdaptorTask
import sys
'''
Created on 08-Feb-2020

@author: deepak
'''
from labs.module03 import TempSensorAdaptorTask
import sys
'''
this python script starts the entire Temperature Hnadling process here. This is the main/start process
'''

sys.path.append('/home/pi/workspace/iot-device/apps')
# print(sys.path)


# instance of temperature Emulator created with threshold value
alert_diff = 0.05
simulator = TempSensorAdaptorTask.TempSensorAdaptorTask(alert_diff)
#thread starting
simulator.start()
# enabled the emulator
simulator.setEmulator(True)
