major = 0
minor = 0
for a in range(1, 6):
    weight = float(input(f"{a}º person weight: "))
    if a == 1:
        major = weight
        minor = weight
    else:
        if weight > major:
            major = weight
        if weight < minor:
            minor = weight
print(f'The major value will be: {major}Kg')
print(f'The minor value will be: {minor}Kg')