import re

batregex = re.compile(r'Bat(wo)*man')

mo1 = batregex.search('The adventures of Batman.')
print(mo1.group())

mo2 = batregex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = batregex.search('The adventures of Batwowowowowoman')
print(mo3.group())


''' For the * there can even be no occurance (as seen for mo2)
	And + will stand for 1 or more occurances, check in the next program.'''