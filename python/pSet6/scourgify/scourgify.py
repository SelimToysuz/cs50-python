import sys
import csv

if len(sys.argv) == 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 4:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1]) as before:
        with open(sys.argv[2], "w") as after:
            students = []
            reader = csv.DictReader(before)
            for row in reader:
                last, first = row["name"].split(",")
                students.append({"first" : first.strip(), "last" : last, "house" : row["house"]})
            writer = csv.DictWriter(after, fieldnames=["first", "last", "house"])
            writer.writeheader()
            for student in students:
                writer.writerow(student)
except FileNotFoundError:
    sys.exit(f"Could not read {sys.argv[1]}")

