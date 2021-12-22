colors = {
    "clean": "\033[m",
    "green": "\033[1:32m",
    "red": "\033[1:31m",
    "yellow": "\033[1:33"
}
print('''This code will show the mayor and the minor number.''')
x = int(input("First: "))
y = int(input("Second: "))
if x > y:
    print(f'{colors["green"]}{x}{colors["clean"]} is more than {colors["red"]}{y}{colors["clean"]}!')
elif y > x:
    print(f'{colors["green"]}{y}{colors["clean"]} is more than {colors["red"]}{x}{colors["clean"]}!')
elif x == y:
    print(f'{colors["green"]}{x}{colors["clean"]} is equal {colors["green"]}{y}{colors["clean"]}')