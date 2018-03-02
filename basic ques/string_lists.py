string = str(input("Enter any string: "))

for palindrome in string:
	if string[::-1] == string:
		print ("This string is a palindrome")
	else:
		print ("This string is not a palindrome")
