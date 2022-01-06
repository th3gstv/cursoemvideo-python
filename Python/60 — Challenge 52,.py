colors = {
    "clean": "\033[m",
    "green": "\033[32m",
    "red": "\033[31m"
}
count = 0
a = int(input('Insert a number: '))
for c in range(1, a + 1):
    if a % c == 0:
        print(f'{colors["green"]}{c}{colors["clean"]}', end=" ")
        count += 1
    else:
        print(f'{colors["red"]}{c}{colors["clean"]}', end=" ")
print(f'\nThe number {a} was divided in {count} times')
if count > 2:
    print(f'{a} is not a prime.')
else:
    print(f'{a} is a prime!')