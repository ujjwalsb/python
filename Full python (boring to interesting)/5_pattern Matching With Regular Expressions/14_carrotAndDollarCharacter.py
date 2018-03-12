import re

beginsWithHello = re.compile(r'^Hello') # ^ stands for start with.
mo1 = beginsWithHello.search('Hello World.')
mo2 = beginsWithHello.search('He said Hello')
print(mo1)
print(mo2)

# Output
''' <_sre.SRE_Match object; span=(0, 5), match='Hello'> '''
''' None '''

print('----------------------------------------------')


endsWithNumber = re.compile(r'^\d+$')
mo3 = endsWithNumber.search('8768767842')
print(mo3)

# Output
''' <_sre.SRE_Match object; span=(0, 10), match='8768767842'> '''