colors = {
    "clean": "\033[m",
    "green": "\033[1;32m",
    "red": "\033[1;31m"
}
sp = int(input("Your speed car: "))
n1 = (sp - 80)*7
if sp <= 80:
    print("{}Everything is right. Keep move on!{}".format(colors["green"], colors["clean"]))
else:
    print("{}We catch you! \n Traffic ticket in U$ {}{}".format(colors["red"], n1, colors["clean"]))
