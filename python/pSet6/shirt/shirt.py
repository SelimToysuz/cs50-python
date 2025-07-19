from PIL import Image, ImageOps
from os import path
import sys

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif path.splitext(sys.argv[1])[1] != path.splitext(sys.argv[2])[1]:
    sys.exit("Input and output have different extensions")
elif path.splitext(sys.argv[1])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")
elif path.splitext(sys.argv[2])[1].lower() not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid input")

try:
    with Image.open(sys.argv[1]) as before:
        with Image.open("shirt.png") as shirt:
            before = ImageOps.fit(before, shirt.size)
            before.paste(shirt, shirt)
            before.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("Input does not exist")

