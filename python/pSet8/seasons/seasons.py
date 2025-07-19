from datetime import date
import inflect
import sys

def main():
    s = input("Please enter your date of birth. (YYYY-MM-DD) ")
    print(seasons(s))

def seasons(birth):
    try:
        birth = date.fromisoformat(birth)
    except ValueError:
        sys.exit("Invalid date")
    now = date.today()
    difference = now - birth
    minutes = difference.days * 24 * 60
    str_minutes = inflect.engine().number_to_words(minutes, andword="")
    return f"{str_minutes.capitalize()} minutes"

if __name__ == "__main__":
    main()
