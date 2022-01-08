s1 = 0
major = 0
minor = 0
majorname = 0
twenty = 0
for p in range(1, 6):
    print(f'----- {p}º PERSON -----')
    n = str(input("Name: "))
    y = int(input("Age: "))
    g = str(input("Gender [M/F]: ")).upper() .strip()
    s1 += y
    s2 = (s1/p)
    #Oldest man
    if p == 1 and g == 'M':
        major = y
        majorname = n
    if g == 'M' and y > major:
        major = y
        majorname = n
    #Woman
    if g == 'F' and y < 20:
        twenty += 1
print(f'The average age is {s2} years')
print(f'The oldest man has {major} years and his name is {majorname}')
print(f'We have {twenty} girls under the 20 years')