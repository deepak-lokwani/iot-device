'''
Created on 19-Apr-2020

@author: deepa
'''
import requests
import logging
import time

logging.disable(logging.DEBUG)
'''
global variables
'''

ENDPOINT = "industrial.api.ubidots.com"
DEVICE_LABEL = "pedestrian-project"
VARIABLE_LABEL = "cpu-utilization"
VARIABLE_LABEL1 = "memory-utilization"
TOKEN = "BBFF-yegKC0ObS7wjfGO8Bx2IU53hjRv9il"
DELAY = 1  # Delay in seconds

'''
this class is used to publish the system performancew data 
to the Ubidots cloud platform using Api client connector
'''
def post_var(payload, url=ENDPOINT, device=DEVICE_LABEL, token=TOKEN):
   
    try:
        url = "http://{}/api/v1.6/devices/{}".format(url, device)
        headers = {"X-Auth-Token": token, "Content-Type": "application/json"}

        attempts = 0
        status_code = 400

        while status_code >= 400 and attempts < 5:
#             print("[INFO] Sending data, attempt number: {}".format(attempts))
            req = requests.post(url=url, headers=headers,
                                json=payload)
            status_code = req.status_code
            attempts += 1
            time.sleep(1)
#         print("[INFO] Results:" + req.text)
    
    except Exception as e:
        print("[ERROR] Error posting system performance details, details: {}".format(e))

def main(cpuUtil, memUtil):

    payload = {VARIABLE_LABEL: cpuUtil}
    payload1 = {VARIABLE_LABEL1: memUtil}
    # Sends data
    post_var(payload)
    post_var(payload1)
    return True


if __name__ == "__main__":
    while True:
        main()
        time.sleep(DELAY)