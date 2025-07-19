str = input("camelCase: ")
print("snake_case: ", end="")
for c in str:
    if c.isupper():
        c = c.lower()
        print(f"_{c}", end="")
    else:
        print(c, end="")
print()
