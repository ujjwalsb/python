import csv

exampleFile = open('example.csv')
exampleReader = csv.reader(exampleFile)
exampleData = list(exampleReader)

print(exampleData)

print("=================")

print(exampleData[0][:])
print(exampleData[6][1])