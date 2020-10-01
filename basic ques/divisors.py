num = int(input("Please enter any number: "))


res = []
for div in range(1,num+1):
	if num % div == 0:
		res.append(div)	
print (res)
