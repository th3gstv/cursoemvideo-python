from time import sleep
colors = {
    "bold": "\033[1m",
    "clean": "\033[m",
    "green": "\033[1;32m"
}
sum = 0
count = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        sum += c
        count += 1
print(f"{colors['bold']}The sum of the {colors['green']}{count}{colors['clean']} {colors['bold']}numbers is:{colors['clean']} {sum}")