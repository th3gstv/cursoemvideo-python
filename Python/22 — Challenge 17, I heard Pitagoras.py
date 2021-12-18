import math
print("-"*50)
print("This program will calculate the triangle hypotenuse!")
print("-"*50)
ca = float(input("Opposite side: "))
co = float(input("Adjacent side: "))
hy = ((ca**2)+(co**2))**0.5
print("Hypotenuse: {:.2f}".format(hy))