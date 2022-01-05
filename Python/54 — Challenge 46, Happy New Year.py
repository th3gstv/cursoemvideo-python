from time import sleep
colors = {
    "yellow": "\033[1;33m",
    "end": "\033[m"
}
for c in range(10, 0, -1):
    print(c, end=' ')
    sleep(1)
print(f'\n {colors["yellow"]}HAPPY NEW YEAR{colors["end"]}!')