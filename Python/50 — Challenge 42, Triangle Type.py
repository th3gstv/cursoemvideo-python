colors = {
    "clean": "\033[m",
    "red": "\033[1;31m",
    "green": "\033[1;32m"
}
a = float(input("1st segment: "))
b = float(input("2nd segment: "))
c = float(input("3rd segment: "))
if b + c > a and b + a > c and c + a > b and a == b and a == c:
    print(f' We will have a {colors["green"]}Equilateral Triangle{colors["clean"]}!')
elif b + c > a and b + a > c and c + a > b and a == b and a != c or b == c and b != a or a == c and a != b:
    print(f' We will have a {colors["green"]}Isosceles Triangle{colors["clean"]}!')
elif b + c > a and b + a > c and c + a > b and a != c and c != b:
    print(f' We will have a {colors["green"]}Scalene Triangle{colors["clean"]}!')
else:
    print(f' {colors["red"]}We cant make a Triangle!{colors["clean"]}')