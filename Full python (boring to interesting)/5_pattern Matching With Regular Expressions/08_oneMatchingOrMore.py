import re

batregex = re.compile(r'Bat(wo)+man')

mo1 = batregex.search('The adventures of Batwoman.')
print(mo1.group())

mo2 = batregex.search('The adventures of Batwowowowowoman')
print(mo2.group())

mo3 = batregex.search('The adventures of Batman')
print(mo3 == None)
