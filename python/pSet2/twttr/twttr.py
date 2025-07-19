vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]
s = input("Input: ")
new = ""
for c in s:
    if c not in vowels:
        new += c
print(new)
