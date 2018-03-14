import csv

outputFile = open('output.csv', 'w')
outputWriter = csv.writer(outputFile)

outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, World!', 'spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.14576, 4])

outputFile.close()