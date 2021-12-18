name=input("Name: ")
print("Be welcome, {}! Here we go calculate your notes and your averege ".format(name))
a=float(input("Your first note: "))
b=float(input("Your second note: "))
#Idk how I can put this values in decimal form
#I got it
c=(a+b)/2
print("With {:.1f} in the fist step and {:.1f} in your second step your avarege will be {:.1f}".format(a,b,c))