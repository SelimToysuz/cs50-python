def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not s.isalnum():
        return False
    if not s[:2].isalpha():
        return False
    if not 2 <= len(s) <=6:
        return False
    for i in range(len(s)):
        if s[i].isdigit():
            if s[i] == "0":
                return False
            for j in s[i+1:]:
                if j.isalpha():
                    return False
            break
    return True


main()
