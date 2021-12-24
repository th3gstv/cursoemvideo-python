colors = {
    "red": "\033[1;31m",
    "green": "\033[1;32m",
    "clean": "\033[m",
    "bold": "\033[1m",
    "yellow": "\033[1;33m"
}
print('='*7, 'Minimalist Store', '='*7)
x = int(input(f' {colors["bold"]}Total price:{colors["clean"]} $'))
print('''WAYS TO PAY IT
[1] With Cash
[2] With Debit Card
[3] 2x In Credit Card 
[4] 3x Or More in Credit Card''')
y = int(input(f' {colors["bold"]}Select the best option for you:{colors["clean"]} '))
if y == 1:
    print(f' Your purchase of {colors["red"]}${x:.2f}{colors["clean"]} will cost {colors["green"]}${0.9*x:.2f}{colors["clean"]}!')
elif y == 2:
    print(f' Your purchase of {colors["red"]}${x:.2f}{colors["clean"]} will cost {colors["green"]}${0.95*x:.2f}{colors["clean"]}!')
elif y == 3:
    print(f' Your purchase of {colors["red"]}${x:.2f}{colors["clean"]} will cost {colors["yellow"]}${x/2:.2f} in 2x{colors["clean"]}')
elif y == 4:
    a = int(input(f' {colors["bold"]}How many times do you want to split?{colors["clean"]} '))
    print(f' Your purchase of {colors["red"]}${x:.2f}{colors["clean"]} will cost {colors["yellow"]}${x*1.2:.2f}{colors["clean"]}. '
          f'\n {colors["green"]}${(x/a)*1.2:.2f}{colors["clean"]} in {colors["yellow"]}{a}x{colors["clean"]}"')
else:
    print(f' {colors["red"]}Invalid. Try again!{colors["clean"]}')