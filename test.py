#!/usr/bin/python
import re
import io
import sys
import fcntl
import time
import copy
import string
from AtlasI2C import (
	 AtlasI2C
)

pH_calibrator = 14.0 / 14.0
DO_calibrator = 14.0 / 14.0
Tmp_calibrator = 14.0 / 14.0

def print_devices(device_list, device):
    for i in device_list:
        if(i == device):
            print("--> " + i.get_device_info())
        else:
            print(" - " + i.get_device_info())
    #print("")
def get_devices():
    device = AtlasI2C()
    device_address_list = device.list_i2c_devices()
    device_list = []
    
    for i in device_address_list:
        device.set_i2c_address(i)
        response = device.query("I")
        moduletype = response.split(",")[1] 
        response = device.query("name,?").split(",")[1]
        device_list.append(AtlasI2C(address = i, moduletype = moduletype, name = response))
    return device_list

def main():
    
    device_list = get_devices()
        
    device = device_list[0]
        
    print_devices(device_list, device)
    
    real_raw_input = vars(__builtins__).get('raw_input', input)  
    while True:
        for dev in device_list:
            dev.write("R")
            time.sleep(1)
        for dev in device_list:
            if dev == device_list[0]:
                extStr = re.findall(r"[-+]?\d*\.\d+|\d+", dev.read())
                DO = float(extStr[1]) * DO_calibrator
                print(DO)
            elif  dev == device_list[1]:
                extStr = re.findall(r"[-+]?\d*\.\d+|\d+", dev.read())
                pH = float(extStr[1]) * pH_calibrator
                print(pH)
            else:
                extStr = re.findall(r"[-+]?\d*\.\d+|\d+", dev.read())
                tmp = float(extStr[1]) * Tmp_calibrator
                print(tmp)
            
        print('\n')
                
if __name__ == '__main__':
    main()