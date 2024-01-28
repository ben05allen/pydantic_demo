import csv
from schedules import Sale


parsed_rows = list()
with open("Sales.csv") as csv_file:
    reader = csv.DictReader(csv_file)
    for row in reader:
        parsed_rows.append(parsed_row := Sale(**row))
        print(parsed_row)
