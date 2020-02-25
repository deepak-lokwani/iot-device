'''
Created on 08-Feb-2020

@author: deepak_lokwani
'''

'''
this python script starts the entire Humidity and Temperature Handling process here. This is the main/start process
'''

from labs.module05 import HumiditySensorAdaptorTask
from labs.module05 import HI2CSensorAdaptorTask
from labs.module05 import TempSensorAdaptorTask
import sys
from time import sleep



sys.path.append('/home/pi/workspace/iot-device/apps')
# print(sys.path)


'''
 instance of temperature and humidity Emulators created with threshold value
'''

simulator = HumiditySensorAdaptorTask.HumiditySensorAdaptorTask()
simulator2 = HI2CSensorAdaptorTask.I2CSenseHatAdaptor()
simulator3 = TempSensorAdaptorTask.TempSensorAdaptorTask(0.1)

# starting my threads
#sleep(2)
#simulator.start()
#sleep(2)
#simulator2.start()
#sleep(2)
simulator3.start()

# enabling the emulators
simulator.setEmulator(True)
simulator2.setEmulator(True)
simulator3.setEmulator(True)
