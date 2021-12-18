a = float(input("First segment: "))
b = float(input("Second segment: "))
c = float(input("Third segment: "))
if a + b > c and b + c > a and a + c > b:
    print("We will have a triangle!")
else:
    print("We do not have a triangle!")