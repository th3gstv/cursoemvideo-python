colors ={
    "red": "\033[1;31m",
    "bold": "\033[1m",
    "clean": "\033[m"
}
kg = float(input(f'{colors["bold"]}Height in kg:{colors["clean"]} '))
m = float(input(f'{colors["bold"]}Weight in meters:{colors["clean"]} '))
bmi = kg / m**2
print(f'{colors["bold"]}Body Mass Index:{colors["clean"]} {bmi:.2f}kg/m²')
if bmi < 18.5:
    print(f' Under Weight!')
elif 18.5 <= bmi < 25:
    print(f' Ideal Weight!')
elif 25 <= bmi < 30:
    print(f' Overweight!')
elif 30 <= bmi <= 40:
    print(f' Obesity!')
else:
    print(f' Morbid Obesity!')