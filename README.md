# Olympus Foot Pedal RS-26 PyUSB Application

PyUSB Python code to read buttons from Olympus Foot Pedal RS-26 USB device, on Windows.
This has been tested on Windows 10 64

Requirements:

1. Install libusbK: https://sourceforge.net/projects/libusbk/

Then:

2. You must setup a driver with: http://zadig.akeo.ie/
  * Make sure the device you are setting up has the "USB ID" 07B4 0202 and you select "libusbK" for the driver

3. PyUSB:
  * Download the zip from here: http://walac.github.io/pyusb/
  * Unzip to a folder then follow these installation instructions:
    * https://github.com/walac/pyusb#installing-pyusb-on-windows
