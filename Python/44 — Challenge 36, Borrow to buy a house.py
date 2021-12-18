colors = {
    "clean": "\033[m",
    "yellow": "\033[1:33m",
    "green": "\033[1:32m",
    "red": "\033[1:31m"
}
print("Accepted or rejected to borrow money bank? Find out now")
house = int(input("How much costs the house? U$"))
x = int(input("How much do you receive? U$"))
time = int(input("How many years do you want to be paying? "))
months = (time*12)
rent = (house/months)
print("It will last {}{}{} months.".format(colors["yellow"], months, colors["clean"]))
if (100*rent)/x <= 30:
    print("The rent value will be {}U${:.2f}{}".format(colors["green"], rent, colors["clean"]))
    print("{}You're accept!{}".format(colors["green"], colors["clean"]))
else:
    print("To buy a U${}{:.2f}{} house in {}{}{} years you'll pay a U${}{:.2f}{} installment .".format(colors["green"], house, colors["clean"], colors["yellow"], time, colors["clean"], colors["red"], rent, colors["clean"]))
    print("{}You're rejected!{}".format(colors["red"], colors["clean"]))
