from random import randint

while True:
    try:
        lv = int(input("Level: "))
        if lv > 0:
            break
    except ValueError:
        pass

num = randint(1, lv)

while True:
    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break
        except ValueError:
            pass
    if guess < num:
        print("Too small!")
    elif guess > num:
        print("Too large!")
    else:
        print("Just right!")
        break
