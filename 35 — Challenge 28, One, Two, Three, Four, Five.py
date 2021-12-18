#import random
#List = [1, 2, 3, 4, 5]
#n2 = (str(random.choice(List)))
#s1 = str(input("Choose a number from 1 to 5: "))
#print("You won!" if s1 == n2 else "You lost!")
#print("The number drawn was {}".format(n2))
from random import randint
from time import sleep
colors = {
    "green": "\033[1;32m",
    "yellow": "\033[1;33m",
    "red": "\033[1;31m",
    "clean": "\033[m",
    "start": "\033[4;34m"
}
pc = randint(0, 5)
print("-="*20)
print("{}I will think a number from 0 to 5, try to discover out!{}".format(colors["start"], colors["clean"]))
print("-="*20)
pl = int(input("What number I thought? "))
print("{}Waiting...{}".format(colors["yellow"], colors["clean"]))
sleep(3)
if pc == pl:
    print("You {}won{}! I thought {} and you're right!".format(colors["green"], colors["clean"], pc))
else:
    print("You {}lost{}! I thought {} and not {}".format(colors["red"], colors["clean"], pc, pl))