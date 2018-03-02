# Exception Handling

def spam(divideBy):
	try:
		return 42 / divideBy
	except ZeroDivisionError:
		print ('Invalid Argument, Division by 0 is not possible')

print (spam(2))
print (spam(12))
print (spam(0))
print (spam(8))