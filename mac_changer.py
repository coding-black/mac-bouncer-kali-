import os
import time

print('\n\n\t\t\tMac Bouncer by Black Coders\n\n')

os.system('ifconfig')

type = input('Enter the interface name :- ')

while True:
	os.system(f'ifconfig {type} down')
	os.system(f'macchanger -r {type}')
	os.system(f'ifconfig {type} up')
	time.sleep(3)