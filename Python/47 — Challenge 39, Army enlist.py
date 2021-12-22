from datetime import date
colors = {
    "clean": "\033[m",
    "bold": "\033[1m"
    }
#print(date.today().year) to show the year
bd = int(input("Birthday year: "))
year = (date.today().year)
age = year-bd
x = bd + 18
y = 18 - age
print(f'Who born in {colors["bold"]}{bd}{colors["clean"]} will have {colors["bold"]}{age}{colors["clean"]} years in {colors["bold"]}{year}{colors["clean"]}.')
if age == 18:
    print(f'You must enlist as soon as possible!')
elif age > 18:
    print(f'Your enlist was in {colors["bold"]}{x}{colors["clean"]}, {colors["bold"]}{year-x}{colors["clean"]} years past!  ')
elif age < 18:
    print(f'You do not have enlist now.\n Wait for {colors["bold"]}{y}{colors["clean"]} years and try again!')