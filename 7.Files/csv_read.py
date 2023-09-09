import csv
with open('D:\python\innovators.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)