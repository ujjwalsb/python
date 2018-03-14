''' Suppose we want to separate cells with a tab character instead of a comma
	and you want the rows to be double spaced. '''

import csv

csvFile = open('delimiLineTerExample.tsv', 'w')		#tsv - tab separated value
csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')

csvWriter.writerow(['apples', 'oranges', 'grapes'])
csvWriter.writerow(['eggs', 'bacon', 'ham'])
csvWriter.writerow(['spam', 'spam', 'spam', 'spam', 'spam', 'spam'])

csvFile.close()