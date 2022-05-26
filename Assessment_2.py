# importing csv module
import csv

# Open file in read mode
file = open('employees.csv', 'r')

# reading csv file and storing the values in list
csv_reader = list(csv.reader(file))
