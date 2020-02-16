'''
Created on 08-Feb-2020

@author: deepak
'''

from labs.module04 import HumiditySensorAdaptorTask
from labs.module04 import HI2CSensorAdaptorTask
from labs.module04 import TempSensorAdaptorTask
import sys
from time import sleep

'''
this python script starts the entire humidity Handling process here. This is the main/start process
'''

sys.path.append('/home/pi/workspace/iot-device/apps')
# print(sys.path)


# instance of temperature Emulator created with threshold value

simulator = HumiditySensorAdaptorTask.HumiditySensorAdaptorTask()
simulator2 = HI2CSensorAdaptorTask.I2CSenseHatAdaptor()
simulator3 = TempSensorAdaptorTask.TempSensorAdaptorTask(0.1)
#thread starting
sleep(2)
simulator.start()
sleep(2)
simulator2.start()
sleep(2)
simulator3.start()

# enabled the emulator
simulator.setEmulator(True)
simulator2.setEmulator(True)
simulator3.setEmulator(True)
