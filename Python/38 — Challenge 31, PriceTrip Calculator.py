ds = int(input("How much quilometers was your trip? "))
if ds <= 200:
    x = 0.5*ds
    print("Will be: U${:.2f}".format(x))
else:
    y = 0.45*ds
    print("Will be: U${:.2f}".format(y))