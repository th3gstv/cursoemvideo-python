import random
print("Jobs is a teacher. He has four students e need one to make a favor. Who do it  for him?")
print("-"*50)
s1 = str(input("Do you remember her name? "))
s2 = str(input("And the name of {}'s friend? ".format(s1)))
s3 = str(input("Who is the children walks with {}? ".format(s2)))
s4 = str(input("And finally, who is te most intelligent class? "))
print("-"*50)
print("Jobs will sort who do it for him...")
lista = [s1, s2, s3, s4]
choosed = random.choice(lista)
print("Will be {}".format(choosed))