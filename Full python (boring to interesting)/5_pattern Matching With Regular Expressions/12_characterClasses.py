import re

xmasRegex = re.compile(r'\d+\s\w+')

mo = xmasRegex.findall('12 drummers, 11 pipers, 10 ladies, 9 maids, 8 rings')
print(mo)