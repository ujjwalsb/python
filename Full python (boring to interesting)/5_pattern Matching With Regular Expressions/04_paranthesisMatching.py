import re

PhoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')

mo = PhoneNumRegex.search('My phone number is (415) 789-8979')

print(mo.group(1))
print(mo.group(2))
