num = int(input("Please enter any number : \n"))
check = num % 2
div = num % 4

if check == 0:
	print ("The number is even")
else:
	print ("The number is odd")

if div ==0:
	print ("The number is multiple of 4")
else:
	print ("The number is not a multiple of 4")
