ph = str(input("What's your favorite phrase? ")).strip() .lower()
print("The letter (a) will repeat", ph.count("a"), "times")
print("The position that (a) will be for the first time is", ph.find("a")+1)
print("The position that (a) will be for the end time is", ph.rfind("a")+1)
