colors = {
    "clean": "\033[m",
    "green": "\033[1;32m",
    "red": "\033[1;31m"
}
from datetime import date
print("This program  inform to you if this year was/will be bissext! \n Press '0' to start with PC configuration...")
y = int(input("Insert a year: "))
if y == 0:
    y = date.today().year
if y % 4 == 0 and y % 100 !=0 or y % 400 == 0:
    print("{}{} is a bissext year!{}".format(colors['green'], y, colors["clean"]))
else:
    print("{}{} isn't a bissext year!{}".format(colors["red"], y, colors["clean"]))