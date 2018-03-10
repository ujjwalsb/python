import re

PhoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = PhoneNumRegex.search('My number is 431-345-4845')

print(mo.group(1))	# Prints the first group 
print(mo.group(2))	# Prints the 2nd group
print(mo.group(0))	# Prints the full group
print(mo.groups())	# Prints the tuple of multiple values

areaCode, mainNumber = mo.groups()	# Notice the plural of group

print('\nThe area Code is: '+areaCode)			# Divides 2 group in particular argument (1st arg)
print('The main Phone Number is: '+mainNumber)		# 2nd Argument