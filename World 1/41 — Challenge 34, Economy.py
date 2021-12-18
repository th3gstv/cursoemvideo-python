colors = {
    "clean": "\033[m",
    "yellow": "\033[4;33m",
    "green": "\033[1;32m",
    }
i1 = int(input("{}How much do you receive?{} ".format(colors["yellow"], colors["clean"])))
if i1 <= 1250:
    x = i1*1.1
    print("{}New Increase (10%): U${:.2f}{}".format(colors["green"], x, colors["clean"]))
else:
    y = i1*1.15
    print("{}New Increase (15%): U${:.2f}{}".format(colors["green"], y, colors["clean"]))