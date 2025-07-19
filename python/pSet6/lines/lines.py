import sys

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) == 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-3:] != ".py":
    sys.exit("Not a Python file")

try:
    with open(sys.argv[1]) as file:
        counter = 0
        for line in file:
            line = line.strip()
            if line not in ["", "\n"] and not line.startswith("#"):
                counter += 1
        print(counter)
except FileNotFoundError:
    sys.exit("File does not exist")


