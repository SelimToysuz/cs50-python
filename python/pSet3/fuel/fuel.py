while True:
    try:
        x, y = map(int, input("Fraction: ").split("/"))
        if y == 0 or x > y:
            raise ValueError
    except ValueError:
        pass
    else:
        break

if x/y <= .01:
    print("E")
elif x/y >= .99:
    print("F")
else:
    print(f"{round(x/y * 100)}%")
