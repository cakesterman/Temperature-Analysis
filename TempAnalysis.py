import sys
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

def read_csv_file():

	with open('temp.csv') as csv_file:

		global data_array
		data_array = []

		csv_reader = csv.reader(csv_file, delimiter = ',')

		line_count = 0
		current_col = 0

		for row in csv_reader:

			temp_array = []
			array_counter = 0

			temp = row[0]
			date = str(row[3])

			temp_array.append(temp)
			temp_array.append(date)

			data_array.append(temp_array)

def anazlyze_24_hour_temps(date_to_analyze):

	day_dict = {}

	date_to_analyze = int(date_to_analyze)

	restrict_dataset_to_n_values = 40

	new_day = False

	counter = restrict_dataset_to_n_values

	for values in data_array:

		new_date_string = ""

		date = values[1]

		# This pulls the date from the string and checks to see if it matches the day the user wants analyzed
		if int(date[8:10]) == date_to_analyze:

			if counter == restrict_dataset_to_n_values:

				print("Adding ", date)

				fahrenheit = round((float(values[0]) * 9 / 5 + 32), 2)

				day_dict[values[1]] = fahrenheit

				counter = 1

			else:

				counter += 1


	print(day_dict)
	print(len(day_dict))

	plot_24hour(day_dict)


def plot_24hour(data_to_plot):

	plt.figure(figsize=(25,15))
	fix, ax = plt.subplots(figsize=(25, 15))

	plt.xticks(rotation='vertical')
	plt.xlabel("Time")
	plt.ylabel("Temperature in Fahrenheit")
	plt.title("Tyler's Room Temperature in a 24 Hour Period")

	plt.plot(list(data_to_plot.keys()), list(data_to_plot.values()))

	ax.yaxis.set_major_locator(ticker.MultipleLocator(1))

	#plt.show()
	plt.savefig('24 Hour Temperature on the {}.png'.format(sys.argv[1]))




read_csv_file()
# User has to pass in a date in the terminal (ex. python3 TempAnalysis.py 25)
anazlyze_24_hour_temps(sys.argv[1])

