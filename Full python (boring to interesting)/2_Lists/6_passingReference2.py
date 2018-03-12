

spam = [1,2,3,4,5]
cheese = spam
cheese[1] = 'Hello'

print(spam)
print(cheese)


'''Well this might seem odd but, the code changed the value of cheese only 
but it seems that it also changed the value of spam !

It is because there is only 1 list not 2, first list reference and 
second list refernce are the same,

To check if how can we change the value of one without the same reference,
the checkout the next program (7_referenceCopy.py).'''