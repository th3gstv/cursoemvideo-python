colors = {
    "clean": "\033[m",
    "yellow": "\033[1:33m",
    "green": "\033[1:32m",
    "red": "\033[1:31m"}
name = str(input("Name: "))
age = str(input("Age: "))
height = str(input("Height: "))
print(f'{colors["yellow"]}Welcome{colors["clean"]}, {name}! You have {age} years and {height}m')