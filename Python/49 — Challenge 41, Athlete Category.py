from datetime import date
#print(date.today().year) to show the year
colors = {
    "clean": "\033[m",
    "bold": "\033[1m"}
y1 = date.today().year
y2 = int(input("Insert your birthday year: "))
x = y1 - y2
if x <= 9:
    print(f' Category: {colors["bold"]}LITTLE{colors["clean"]}!'
          f' The athlete has {x} years.')
elif 9 < x <= 14:
    print(f' Category: {colors["bold"]}CHILD{colors["clean"]}!'
          f' The athlete has {x} years.')
elif 14 < x <= 19:
    print(f' Category: {colors["bold"]}JUNIOR{colors["clean"]}!'
          f' The athlete has {x} years.')
elif 19 < x <= 25:
    print(f' Category: {colors["bold"]}SENIOR{colors["clean"]}!'
          f' The athlete has {x} years.')
elif x > 25:
    print(f' Category: {colors["bold"]}MASTER{colors["clean"]}!'
          f' The athlete has {x} years.')