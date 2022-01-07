colors = {
    "green": "\033[1;32m",
    "red": "\033[1;31m",
    "clean": "\033[m"
}
a = str(input("Type one phrase: ")).upper().strip()
b = a.split()
c = ''.join(b)
print(f'The inverse of {c} is {c[::-1]}')
if a == a[::-1]:
    print(f'{colors["green"]}We have a Palindrome!{colors["clean"]}')
else:
    print(f"{colors['red']}We hasn't a Palindrome!{colors['clean']}")