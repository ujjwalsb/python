list = [1,2,4,6,4,2,8,9,0,6,8,4,3,5]
print (list)
num = int(input("Enter a no. to limit the list: "))

res = []
for less in list:
	if less < num:
		res.append(less)		 
		print (less)
