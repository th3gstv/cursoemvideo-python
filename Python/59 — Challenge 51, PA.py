count = 0
sum = 0
print('='*15)
print("Arithmetic Progression")
print('='*15)
a1 = int(input("First term: "))
r = int(input("Reason: "))
for c in range(0, 10):
    count += 1
    x = a1 + (count-1)*r
    print(x, end=' 🠒 ')
print('END!')