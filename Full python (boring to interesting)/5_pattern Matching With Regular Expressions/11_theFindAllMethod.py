import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')	# No Group
mo1 = phoneNumRegex.findall('Cell: 453-876-8738, Work: 987-348-4878')
print(mo1)

print('-----------------------------------------')

phoneNumRegexGr = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
mo2 = phoneNumRegexGr.findall('Cell: 899-878-8389, Work: 897-799-9708')
print(mo2)