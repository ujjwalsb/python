import re

greedyHaRegex = re.compile(r'(ha){3,5}')

mo1 = greedyHaRegex.search('hahahahaha')
print(mo1.group())


nongreedyHaRegex = re.compile(r'(ha){3,5}?')

mo2 = nongreedyHaRegex.search('hahahahaha')
print(mo2.group())