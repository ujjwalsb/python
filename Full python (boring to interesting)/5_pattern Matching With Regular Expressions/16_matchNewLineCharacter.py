import re

print('------sample------')
noNewLineRegex = re.compile(r'.*')
mo1 = noNewLineRegex.search('Serve the public trust.\nProtect the innocent.')
print(mo1.group()+'\n')

print('------Accepts Space and new line------')
newLineRegex = re.compile(r'.*', re.DOTALL)
mo2 = newLineRegex.search('Serve the public trust.\nProtect the innocent.')
print(mo2.group()+'\n')