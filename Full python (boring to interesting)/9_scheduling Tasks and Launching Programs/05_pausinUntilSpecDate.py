import datetime
import time

xmas2018 = datetime.datetime(2018, 12, 25, 0, 0, 0)
while datetime.datetime.now() < xmas2018:
 	time.sleep(1) 

 	# This program will be paused until the Xams date date arrives.