######
#this is the moisture sensor script by the end of the 3rd episode in the series called:
#Moisture Sensor Automation and Accuracy Quick-Fix (Raspberry Pi autogardener project ep#3)
######

#importing stuff
import time
import board
import busio
from adafruit_seesaw.seesaw import Seesaw
from datetime import datetime

#i2c setup
i2c_bus = busio.I2C(board.D3, board.D2)
ss = Seesaw(i2c_bus, addr=0x36)

#read moisture level -- 5 samples
moisture_list = []
for i in range(5):
	moisture_list.append(ss.moisture_read())
	time.sleep(5)

#averaging moisture level
touch = sum(moisture_list)/len(moisture_list)

#read temperature
temp = ss.get_temp()

#what time is it
date_var = datetime.now().isoformat(' ')

#printing stuff
print(date_var, str(temp), str(touch))
