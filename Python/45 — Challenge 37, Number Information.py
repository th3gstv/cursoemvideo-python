colors = {
    "clean": "\033[m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "red": "\033[1;31m"
}
number = int(input("Say a whole number: "))
print('''Choose one to converter:
[1] converter to {}Binary{}
[2] converter to {}Octal{}
[3] converter to {}Hexadecimal{}'''.format(colors["green"], colors["clean"], colors["red"], colors["clean"], colors["yellow"], colors["clean"]))
num = int(input("Your choice: "))
if num == 1:
    print("{} to binary is {}!".format(number, bin(number)[2:]))
elif num == 2:
    print("{} to octal is {}!".format(number, oct(number)[2:]))
elif num == 3:
    print("{} to hexadecimal is {}!".format(number, hex(number)[2:]))
else:
    print("{}Error. Try again!{}".format(colors["red"], colors["clean"]))