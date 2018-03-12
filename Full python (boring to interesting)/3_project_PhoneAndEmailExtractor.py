# !/usr/bin/python3
import pyperclip, re

phoneRegex = re.compile(r'''(
	(\d{3}|\(\d{3}\))?					# area code
	(\s|-|\.)?							# separator
	(\d{3})								# first 3 digits
	(\s|-|\.)							# separator
	(\d{4})								# last 4 digits
	(\s*(ext|x|ext.)\s*(\d{2,5}))?		# extension
	)''', re.VERBOSE)

emailRegex = re.compile(r'''(
	[a-zA-Z0-9._%+-]+					# username
	@									# @ symbol
	[a-zA-Z0-9.-]+						# domail name
	(\.[a-zA-z]{2,4})					# dot something
	)''', re.VERBOSE)


# Find match
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
	phoneNum = '-'.join([groups[1], groups[3], groups[5]])
	if groups[6] !='':
		phoneNum += 'x' + groups[6]
	matches.append(phoneNum)

for groups in emailRegex.findall(text):
	matches.append(groups[0])


# Copying results to the clipboard.
if len(matches) > 0:
	pyperclip.copy('\n'.join(matches))
	print('Copied to clipboard:')
	print('\n'.join(matches))
else:
	print('No phone numbers or email addresses found!')


# To run this program first copy the contact us page data from
# any of your site and the run the code to see it working.