import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
   if test := re.search(r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$", ip):
    for part in test.groups():
        if int(part) not in range(256):
           return False
    return True
   else:
      return False


if __name__ == "__main__":
    main()
