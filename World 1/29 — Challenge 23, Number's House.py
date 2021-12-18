print("First Rule — Only numbers with 4 digits")
print("-"*50)

a = input('Say a number: ')
print("Your number was: {}".format(a))

print("Unit:", a[3])
print("Dozen:", a[2])
print("Hundred:", a[1])
print("Thousand:", a[0])