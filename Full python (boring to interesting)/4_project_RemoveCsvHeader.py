# !/usr/bin/python3
# Removes the header from all CSV files in the current directory.
import csv, os

os.makedirs('project_4_sample_folder', exist_ok=True)

# Loop through every file in current directory.
for csvFilename in os.listdir('.'):
	if not csvFilename.endswith('.csv'):
		continue							# Skip non-csv file.

	print('Removing header from ' + csvFilename + '...')


# Read the CSV file in (Skipping first row).
csvRows = []
csvFileObj = open(csvFilename)
readerObj = csv.reader(csvFileObj)

for row in readerObj:
	if readerObj.line_num == 1:
		continue							# skip first row.
	csvRows.append(row)

csvFileObj.close()


# Write out the CSV file.
csvFileObj = open(os.path.join('project_4_sample_folder', csvFilename), 'w')
csvWriter = csv.writer(csvFileObj)

for row in csvRows:
	csvWriter.writerow(row)

csvFileObj.close()