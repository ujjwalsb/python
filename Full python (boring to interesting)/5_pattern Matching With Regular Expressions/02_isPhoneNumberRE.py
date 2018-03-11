import re

# Here r defines as a 'raw' and d stands for 'digit'
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

mo = phoneNumRegex.search('My number is 415-555-4109.')
print('Phone Number Found: ' + mo.group())
