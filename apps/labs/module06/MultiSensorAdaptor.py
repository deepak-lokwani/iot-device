'''
Created on 29-Feb-2020

@author: deepa
'''
'''
this python script starts the Temperature Handling process here. This is the main/start process
'''

from labs.module06 import TempSensorAdaptorTask
import sys
from time import sleep

sys.path.append('/home/pi/workspace/iot-device/apps')
# print(sys.path)

'''
instance of temperature and humidity Emulators created with threshold value
'''

simulator3 = TempSensorAdaptorTask.TempSensorAdaptorTask(0.1)

simulator3.start()

# enabling the emulators

simulator3.setEmulator(True)
