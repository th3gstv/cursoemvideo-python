colors = {
    "clean": "\033[m",
    "green": "\033[1;32m",
    "yellow": "\033[1;33m"
}
print("-"*60)
print("You've rend a car who costs {}$60{} per day and {}$0.15{} KM.".format(colors["green"], colors["clean"], colors["yellow"], colors["clean"]))
print("-"*60)
a = int(input("Days using the car: "))
b = float(input("Kilometers driving: "))
x = (60*a)+(0.15*b)
print("You've to pay {}${:.2f}{} to rent a car per {}{:.0f}{} days and driving {}{:.2f}{}km".format(colors["green"], x, colors["clean"], colors["yellow"], a, colors["clean"], colors["yellow"], b, colors["clean"]))