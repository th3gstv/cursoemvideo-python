import random
from time import sleep
colors = {
    "red": "\033[1;31m",
    "clean": "\033[m",
    "yellow": "\033[1;33m",
    "green": "\033[1;32m",
    "bold": "\033[1m"
}
print(f'''
{colors["bold"]}JOKENPO OPTIONS:{colors["clean"]}
[1] Rock
[2] Paper
[3] Scissor
''')
pc = ["Rock", "Paper", "Scissor"]
x = int(input(f' {colors["bold"]}Choose one:{colors["clean"]} '))
y = random.choice(pc)
if x == 1:
    print(f' {colors["green"]}Player played ROCK!{colors["clean"]}')
    sleep(1)
    if y == pc[0]:
        print(f' {colors["yellow"]}PC played ROCK!{colors["clean"]}')
        print(f' {colors["yellow"]}TIE!{colors["clean"]}')
    elif y == pc[1]:
        sleep(1)
        print(f' {colors["yellow"]}PC played PAPER!{colors["clean"]}')
        print(f' {colors["red"]}You LOST!{colors["clean"]}')
    elif y == pc[2]:
        sleep(1)
        print(f' {colors["red"]}PC played SCISSOR!{colors["clean"]}')
        print(f' {colors["green"]}You WON!{colors["clean"]}')
if x == 2:
    print(f' {colors["green"]}Player played PAPER{colors["clean"]}')
    sleep(1)
    if y == pc[0]:
        sleep(1)
        print(f' {colors["yellow"]}PC played ROCK!{colors["clean"]}')
        print(f' {colors["green"]}You WON!{colors["clean"]}')
    elif y == pc[1]:
        sleep(1)
        print(f' {colors["yellow"]}PC played PAPER!{colors["clean"]}')
        print(f' {colors["yellow"]}TIE!{colors["clean"]}')
    elif y == pc[2]:
        sleep(1)
        print(f' {colors["yellow"]}PC played SCISSOR!{colors["clean"]}')
        print(f' {colors["red"]}You LOST!{colors["clean"]}')
if x == 3:
    print(f' {colors["green"]}Player played SCISSOR!{colors["clean"]}')
    if y == pc[0]:
        print(f' {colors["yellow"]}PC played ROCK!{colors["clean"]}')
        print(f' {colors["red"]}You LOST!{colors["clean"]}')
    if y == pc[1]:
        print(f' {colors["yellow"]}PC played PAPER!{colors["clean"]}')
        print(f' {colors["green"]}You WON!{colors["clean"]}')
    if y == pc[2]:
        print(f' {colors["yellow"]}PC played SCISSOR!{colors["clean"]}')
        print(f' {colors["yellow"]}TIE!{colors["clean"]}')
