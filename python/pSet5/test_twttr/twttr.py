def main():
    s = input("Input: ")
    print(shorten(s))

def shorten(word):
    vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
    new = ""
    for c in word:
        if c not in vowels:
            new += c
    return new

if __name__ == "__main__":
    main()
