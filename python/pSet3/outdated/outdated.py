months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"]


while True:
    str = input("Date: ")
    if str[0].isdigit():
        try:
            month, day, year = map(int, str.split("/"))
        except ValueError:
            
    else:
        month, year = str.split(",")
        year = int(year.strip())
        month, day = month.split(" ")
        day = int(day.strip())
        month = months.index(month) +1

    if day<31 and month<13:
        break

print(f"{year}-{month:02}-{day:02}")
