import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if clock := re.search(r"(\d{1,2}):?(\d{2})? (AM|PM) to (\d{1,2}):?(\d{2})? (AM|PM)", s):
        hour1, minute1, setup1, hour2, minute2, setup2 = clock.groups()
        minute1, minute2, hour1, hour2 = minute1 or "00", minute2 or "00", int(hour1), int(hour2)
        if hour1 not in range(1, 13) or hour2 not in range(1, 13):
            raise ValueError("Hours must be between 1 and 12")
        if int(minute1) not in range(60) or int(minute2) not in range(60):
            raise ValueError("Minutes must be between 0 and 59")
        hour1 = hour1 + (12 if setup1 == "PM" else 0)
        hour2 = hour2 + (12 if setup2 == "PM" else 0)
        if hour1 in[12, 24]:
            hour1 -= 12
        if hour2 in [12, 24]:
            hour2 -= 12
        return f"{hour1:02}:{minute1:02} to {hour2:02}:{minute2:02}"
    else:
        raise ValueError

if __name__ == "__main__":
    main()
