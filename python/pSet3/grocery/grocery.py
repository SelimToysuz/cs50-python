items = {}
while True:
    try:
        item = input().upper()
    except EOFError:
        alphabetic = sorted(items.keys())
        for str in alphabetic:
            print(f"{items[str]} {str}")
        break
    else:
        if item in items:
            items[item] += 1
        else:
            items[item] = 1

