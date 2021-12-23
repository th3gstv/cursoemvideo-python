a = float(input("1st segment: "))
b = float(input("2nd segment: "))
c = float(input("3rd segment: "))
if b + c > a and b + a > c and c + a > b:
    print(f' It will exist')
else:
    print(f' It wont exist.')