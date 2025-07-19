names = []
while True:
    try:
        s = input()
        names.append(s)
    except EOFError:
        break

print(f"Adieu, adieu, to {names[0]}", end="")

for name in names[1:-1]:
    print(f", {name}", end="")
    
if len(names) == 2:
    print(f" and {names[-1]}")
elif len(names) > 2:
    print(f", and {names[-1]}")
else:
    print()
