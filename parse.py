import csv
from schedules import Sale


def main():
    parsed_rows = list()
    with open("Sales.csv") as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            parsed_rows.append(Sale(**row))

    for parsed_row in parsed_rows:
        print(parsed_row)


if __name__ == "__main__":
    main()
