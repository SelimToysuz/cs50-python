import random


def main():
    lv = get_level()
    score = 10
    for _ in range(10):
        x = generate_integer(lv)
        y = generate_integer(lv)
        for i in range(3):
            print(f"{x} + {y} = ", end="")
            guess = -1
            try:
                guess = int(input())
            except ValueError:
                pass
            if guess == x+y:
                break
            print("EEE")
            if i == 2:
                print(f"{x} + {y} = {x+y}")
                score -= 1
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            lv = int(input("Level: "))
            if 1 <= lv <= 3:
                break
        except ValueError:
            pass
    return lv

def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError
if __name__ == "__main__":
    main()
