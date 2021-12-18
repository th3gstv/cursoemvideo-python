#U$1 = R$ 5,6
w=int(input("In R$, how much manny has in your wallet: "))
d=w/5.6
#Wrong Code: print("You can trade yours R${} to U$ {(:.2f)}".format(w,d))
print("You can trade yours \033[1;31mR${:.2f}\033[m to \033[1;32mU$ {:.2f}\033[m".format(w,d))

