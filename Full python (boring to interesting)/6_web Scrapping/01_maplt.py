# !/usr/bin/python3
# 1_maplt.py - Launches a map in the browser using address from 
# commandline or clipboard.

import webbrowser, sys, pyperclip

if len(sys.argv) > 1:
	# Get address from command line.
	address = ' '.join(sys.argv[1:])	# Its not 0 index because it will contain the name of the file in commandline and we don't need that.
	print(address)
else:
	# Get address from clipboard.
	address = pyperclip.paste()

webbrowser.open('https://www.google.com/maps/place/' + address)


# ================================================================
'''
1. Go in the command line and type:
	python3 <file_name> <location_name(if any)>
	python3 maplt.py Bangalore

2. The second method you can use is copy the name of the place
3. Then, go in the command line and type only:
	python3 maplt.py

4. The location address will be taken from your clipboard.'''