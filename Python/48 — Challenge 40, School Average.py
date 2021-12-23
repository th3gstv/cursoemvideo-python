colors = {
    "clean": "\033[m",
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m"}
print("Format note: 1 to 10!")
n1 = int(input("1st note: "))
n2 = int(input("2nd note: "))
m = (n1+n2)/2
if m >= 7:
    print(f'{colors["green"]}You are approved!{colors["clean"]}'
          f' Your average was {colors["green"]}{m}{colors["clean"]}')
elif 5 <= m <= 6.9:
    print(f'You are in recovery with {colors["yellow"]}{m}{colors["clean"]} points.')
elif m < 5:
    print(f'{colors["red"]}Reproved!'
    f' You have {m} points!{colors["clean"]}')
