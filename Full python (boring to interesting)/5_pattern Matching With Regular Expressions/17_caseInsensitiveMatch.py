import re

robocop = re.compile(r'robocop', re.I)	# re.I or re.IGNORECASE.

mo1 = robocop.search('RoboCop is part man, part machine, all cop.').group()
print(mo1)

mo2 = robocop.search('ROBOCOP protects the Innocent.').group()
print(mo2)

mo3 = robocop.search('Why does your programs talk about robocop \
						so much ?').group()
print(mo3)