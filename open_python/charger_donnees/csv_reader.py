import csv

with open('C:/Users/PC-16/Desktop/open_python/charger_donnees/data.csv', mode='r') as file:
    csv_reader = csv.reader(file)
    for line in csv_reader:
        print(line)
