import re

atRegex = re.compile(r'.at')	# Here .(dot) is every char except new line.
mo1 = atRegex.findall('The cat in the hat, sat on a flat mat.')
print(mo1)

print('\n<------------------ Dot Star ------------------------>')

# *(star) is zero or more preceeding character / Uses greedy method.
nameregex = re.compile(r'First Name: (.*), Last Name: (.*)')
mo2 = nameregex.search('First Name: Ujjwal, Last Name: Singh')
print(mo2.group(1))
print(mo2.group(2))


print('\n<----------- Greedy and Non-Greedy ------------------>')


nongreedyRegex = re.compile(r'<.*?>')
mo3 = nongreedyRegex.search('<To server man> for dinner.>')
print(mo3.group())


greedyRegex = re.compile(r'<.*>')
mo4 = greedyRegex.search('<To serve man> for dinner.>')
print(mo4.group())