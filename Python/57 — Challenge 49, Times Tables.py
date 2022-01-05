a = int(input("Choose a number: "))
count = -1
for c in range(0, a*11, a):
    count = count + 1
    print(f'{a} x {count} = {c}')