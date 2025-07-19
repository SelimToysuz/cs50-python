from tabulate import tabulate
import sys
import csv

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as file:
        table = []
        reader = csv.reader(file)
        for row in reader:
            table.append(row)

    print(tabulate(table, headers="firstrow", tablefmt="grid"))

except FileNotFoundError:
    sys.exit("File does not exit")
