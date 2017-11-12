num = int(input("Please enter any number: "))
x = list(range(1,num+1))

res = []
for div in x:
	if num % div == 0:
		res.append(div)	
print (res)
