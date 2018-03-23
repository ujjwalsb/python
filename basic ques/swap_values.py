
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

temp = num1
num1 = num2
num2 = temp

print ("Now, first no. is: ", num1)
print ("and second no. is: ", num2)


print("===================OR========================")

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

x,y = y,x

print("Now, the first number is: ", x)
print("Now the second number is: ", y)