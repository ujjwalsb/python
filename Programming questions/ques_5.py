# Define a class which has at least two methods:
# getString: to get a string from console input
# printString: to print the string in upper case.
# Also please include simple test function to test the class methods.

# Solution:

class GetPrint(object):
	def __init__(self):
		self.s = ""

	def getString(self):
		self.s = raw_input("Enter any string: ")

	def printString(self):
		print self.s.upper()

obj = GetPrint()
obj.getString()
obj.printString()