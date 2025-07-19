def main():
    s = input("Greeting: ")
    print("$", value(s))

def value(greeting):
    greeting = str(greeting).lower().split()
    if not greeting:
        return 100
    elif greeting[0].strip(".,!") == "hello":
        return 0
    elif greeting[0][0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
