import time
import os

try:
	while True:
		# write 0 in PWR LED
		os.system('echo 0 | sudo tee /sys/class/leds/PWR/brightness')
		time.sleep(0.4)
		# write 1 in PWR LED
		# toggle led after each 1 second
		os.system('echo 1 | sudo tee /sys/class/leds/PWR/brightness')
		time.sleep(0.4)
except KeyboardInterrupt:
	print("Exiting code")
# reset PWR LED to 1 again.
os.system('echo 1 | sudo tee /sys/class/leds/PWR/brightness')



