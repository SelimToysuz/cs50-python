def main():
    fuel_level = convert(input("Fraction: "))
    print(gauge(fuel_level))


def convert(fraction):
    x, y = map(int, fraction.split("/"))
    if y == 0:
        raise ZeroDivisionError
    if x > y:
        raise ValueError("Fuel cannot exceed maximum value")
    return round(100 * x/y)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
