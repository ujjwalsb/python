import re

haRegex = re.compile(r'(ha){3}')

mo1 = haRegex.search('hahaha')
print(mo1.group())

mo2 = haRegex.search('ha')
print(mo2 == None)