import csv

nicknames = ['Salman', 'Mohit', 'Vinay', 'Vilas']

with open('Santa_Choose.csv', 'w') as csvfile:
	writeCSV = csv.writer(csvfile)

	writeCSV.writerow(['Nicknames', 'Chosen Nicknames'])

	for nickname in nicknames:
		writeCSV.writerow([nickname])
