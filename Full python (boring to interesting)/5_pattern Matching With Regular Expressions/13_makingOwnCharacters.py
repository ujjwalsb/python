import re

# To check VOWEL in a string.
vowelRegex = re.compile(r'[aeiouAEIOU]')
mo1 = vowelRegex.findall('RoboCop eats baby food. BABY FOOD')
print(mo1)


# To check NON-VOWEL in a string.
consonant = re.compile(r'[^aeiouAEIOU]')
mo2 = consonant.findall('RoboCop eats baby food. BABY FOOD')
print(mo2)