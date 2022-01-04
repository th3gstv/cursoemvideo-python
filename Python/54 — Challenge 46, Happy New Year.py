from time import sleep
colors = {
    "yellow": "\033[1;33m",
    "end": "\033[m"
}
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print(f'{colors["yellow"]}HAPPY NEW YEAR{colors["end"]}!')