import re

heroRegex = re.compile(r'Batman|Superman')

mo1 = heroRegex.search('Batman and Superman.')
print(mo1.group())

mo2 = heroRegex.search('Superman and Batman.')
print(mo2.group())


print('---------------------------------------------------------')

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = batRegex.search('Batman lost a wheel.')

print(mo.group())
print(mo.group(1))