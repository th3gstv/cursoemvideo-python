from time import sleep
a = int(input("Insert your first number: "))
b = int(input("Second number: "))
c = int(input("Third number: "))
if a < b and a < c:
    shortest = a
if b < a and b < c:
    shortest = b
if c < a and c < b:
    shortest = c
print("The shortest number will be...")
sleep(2)
print("{}".format(shortest))
if a > b and a > c:
    most = a
if b > a and b > c:
    most = b
if c > a and c > b:
    most = c
sleep(1)
print("The most number will be...")
sleep(1)
print("{}".format(most))