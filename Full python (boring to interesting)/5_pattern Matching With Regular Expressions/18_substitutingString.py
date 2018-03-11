import re

nameRegex = re.compile(r'Agent \w+')
mo1 = nameRegex.sub('Censored','Agent Alice gave the secret documents to Agent Bob')
print(mo1)


agentNamesRegex = re.compile(r'Agent (\w)\w*')
mo2 = agentNamesRegex.sub(r'\1****','Agent Alice told Agent Carol that Agent Eve knew Agent Bob was a double Agent.')
print(mo2)