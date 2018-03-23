'''A Narcissistic Number is a number which is the sum of its own digits, 
each raised to the power of the number of digits.
For example, take:

 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

The Challenge:
Your code must return true or false depending upon whether the given number 
is a Narcissistic number.
Error checking for text strings or other invalid inputs is not required, 
only valid integers will be passed into the function.
'''

def narcissistic( value ):
	total = []
	power = int(len(str(value)))
	digits = [int(x) for x in str(value)]
	for i in digits:
		product = i**power
		total.append(product)
		sumtotal = sum(total)

	if sumtotal == value:
		return True
	else:
		return False

num1 = narcissistic(153)
num2 = narcissistic(1634)
num3 = narcissistic(345)

print(num1)
print(num2)
print(num3)