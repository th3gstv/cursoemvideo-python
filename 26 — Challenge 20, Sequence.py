import random
a = str(input("First student: "))
b = str(input("Second student: "))
c = str(input("Third student: "))
d = str(input("Fourth student: "))
eg = [a, b, c, d]
random.shuffle(eg)
print("The sequence will be: ")
print(eg)