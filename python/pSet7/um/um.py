def main():
    print(count(input("Text: ")))


def count(s):
    text = s.strip().lower().split(" ")
    counter = 0
    for word in text:
        if word.strip(".,?!") == "um":
            counter +=1
    return counter


if __name__ == "__main__":
    main()
