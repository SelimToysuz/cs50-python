x, z, y = input("Expression: ").split()
x = int(x)
y = int(y)

if z == "+":
    print(f"{x + y:.1f}")
elif z == "-":
    print(f"{x - y:.1f}")
elif z == "*":
    print(f"{x * y:.1f}")
elif z == "/":
    print(f"{x / y:.1f}")

