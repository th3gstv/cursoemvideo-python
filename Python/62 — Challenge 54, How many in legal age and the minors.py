from datetime import date
count = 0
#Adults
a1 = 0
#Youngs
a2 = 0
x = date.today().year
for c in range(0, 7):
    count += 1
    a = int(input(f'{count}º Person Birthday Year: '))
    y = (x-a)
    if y >= 18:
        a1 += 1
    else:
        a2 += 1
print(f'We have {a1} adults in legal age and {a2} minors.')