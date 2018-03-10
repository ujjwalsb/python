#! /usr/bin/python3
#1_project_passwordLocker.py

locker = {'ujjwalsingh15@gmail.com': 'qwerty12345',
		'blog': 'qwerty',
		'luggage': '12345'}

import sys, pyperclip
if len(sys.argv) < 2:
	print('Usage: python 1_project_passwordLocker.py [account] - copy account password')
	sys.exit()

account = sys.argv[1]

if account in locker:
	pyperclip.copy(locker[account])
	print('password for ' + account + ' copied to Clipboard')

else:
	print('There is no account named ' + account)

# ---------------------------------------------------------------

''' Edit the contents of dictionary as per your credentials.
		To run this program go to the terminal and type:

			$ python3 1_project_passwordLocker.py ujjwalsingh15@gmail.com
							OR
			$ python3 1_project_passwordLocker.py blog

		to copy the respective values of the keys mentioned. '''