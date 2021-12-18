n1 = float(input("First value: "))
n2 = float(input("Second value: "))
m = (n1+n2)/2
print("Your avarage was {:.1f}".format(m))
print("Nice! Keep it as!" if m >= 6 else "Study more")
#if m >= 6:
#        print("Nice! Keep it as ")
#else:
#    print("Don't give up, study a little bit")