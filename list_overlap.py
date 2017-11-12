list1 = [1,2,3,4,5]
list2 = [1,2,3]

list3=[]
for x in list1:
	if x in list2:
		list3.append(x)
print (list3)
