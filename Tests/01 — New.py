name = str(input("What's your name? "))
if name == "Gustavo":
    print("Hello, Gustavo! \n Nice name!")
elif name == "Anny" or name == "Claudia" or name == "Lara" or name == "Eduardo":
    print("You're Gustavo's family!")
elif name in "Darlon Juscileia Samuel":
    print("You're too Gustavo's family!")
else:
    print("Welcome, {}!".format(name))