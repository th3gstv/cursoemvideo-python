from time import sleep
number = int(input("Say me a number: "))
x = number % 2
if x == 0:
    print("{} is...".format(number))
    sleep(3)
    print("PAIR!")
else:
    print("{} is!".format(number))
    sleep(3)
    print("ODD!")