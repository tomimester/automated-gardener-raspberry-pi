#I followed this tutorial: https://learn.adafruit.com/adafruit-stemma-soil-sensor-i2c-capacitive-moisture-sensor/python-circuitpython-test#circuitpython-and-python-usage-3009830-9
#But I modified the code a bit.

import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw

i2c_bus = busio.I2C(board.D3, board.D2)
ss = Seesaw(i2c_bus, addr=0x36)

while True:
    # read moisture level through capacitive touch pad
    touch = ss.moisture_read()

    # read temperature from the temperature sensor
    temp = ss.get_temp()

    print("temp: " + str(temp) + "  moisture: " + str(touch))

    if touch < 400:
    	print('watering is needed')
    else:
    	print('watering is not needed for now')


    time.sleep(1) 
