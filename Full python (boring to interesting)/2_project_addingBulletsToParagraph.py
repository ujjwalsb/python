# ! /usr/bin/python3

import pyperclip

# First copy the lists from anywhere
text = pyperclip.paste()

# Separate lines and add stars
lines = text.split('\n')

# loop through all indexes in lines lists
for i in range(len(lines)):
	lines[i] = '*' + lines[i]	#Add star to each strings in lines list

text = '\n'.join(lines)
pyperclip.copy(text)