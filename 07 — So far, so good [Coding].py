#Break lines: \n
#Don't break lines: end= '  '
n1=int(input("Choose a number: "))
n2=int(input("Choose another number: "))
s=n1+n2
d=n1-n2
p=n1*n2
dx=n1/n2
print("The first number was {} and the second was {}, well the sum will be {}".format(n1,n2,s))
print("The difference between these two numbers is {} and the product is simple, being {} and the division is {:.3f}".format(d, p,dx))
#My error was put the sentence inside the format
#To make right, I has to put inside the "{}"
