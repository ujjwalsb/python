# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24

# Solution :

import math

c = 50
h = 30
ans = []
i = [x for x in raw_input("Enter Your numbers: ").split(',')]

for d in i:
	ans.append(str(int(round(math.sqrt((2*c*float(d))/h)))))
	
print ','.join(ans)

