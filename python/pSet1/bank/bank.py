str = input("Greeting: ").lower().split()
if str[0] == "hello" or str[0] == "hello,":
    print("$0")
elif str[0][0] == "h":
    print("$20")
else:
    print("$100")
