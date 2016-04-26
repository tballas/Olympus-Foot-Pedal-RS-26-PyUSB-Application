"""
PyUSB Python code to read buttons from Olympus Foot Pedal RS-26 USB device, on Windows. Tested on Windows 10 64

Author: tballas

Requirements:
1. Install libusbK: https://sourceforge.net/projects/libusbk/

Then:
2. You must setup a driver with: http://zadig.akeo.ie/
	Make sure the device you are setting up has the "USB ID" 07B4 0202 and you select "libusbK" for the driver

3. PyUSB: 
	Download the zip from here: http://walac.github.io/pyusb/
	Unzip to a folder then follow these installation instructions: https://github.com/walac/pyusb#installing-pyusb-on-windows
"""

from __future__ import print_function
import usb.core
import usb.util
import sys

deviceCode = "FootPedal"

# Modify these to do whatever you want
def leftButton (): print(deviceCode + '.' + "LeftButton" + '.' + str(keycode[2]))
def middleButton (): print(deviceCode + '.' + "MiddleButton" + '.' + str(keycode[2]))
def rightButton (): print(deviceCode + '.' + "RightButton" + '.' + str(keycode[2]))

def errhandler ():
   pass

# Dictionary of actions
keyactions = {
    8: leftButton,
    2: middleButton,
    4: rightButton
}


VID = 0x07B4	#	Vendor ID for:	OLYMPUS CORPORATION
PID = 0x0202	#	Product ID for:	Foot Pedal RS-26
Endpoint = 0x83	#	Endpoint into Host, Interrupt Transfer Type


# Find device
dev = usb.core.find(idVendor=VID, idProduct=PID)
 
# Check results of find
if dev is None:
	raise ValueError('Device not found')

print("We've found the device")

dev.set_configuration()

# Read the data
try:
	while True:
		keycode = dev.read(Endpoint,8)
		keyactions.get(keycode[2],errhandler)()
except KeyboardInterrupt:
	exit(0)