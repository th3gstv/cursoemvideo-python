from math import sin, cos, tan, radians
print("-"*50)
print("This program will calculate the seno, cosseno and tangent of a any number")
c1 = float(input("Type a angle: "))
s = sin(radians(c1))
c = cos(radians(c1))
t = tan(radians(c1))
print("The {:.0f}º angle will have: \n Sine: {:.2f} \n Cosine: {:.2f} \n Tangent: {:.2f}.".format(c1, s, c, t))