oldest = 0
oldestname = 0
y = 0
qwoman = 0
for p in range(1, 5):
    print("----- {}º Person -----".format(p))
    name = str(input("Name: "))
    years = int(input("Age: "))
    gender = str(input("Masculine/Female: ")).strip().upper()
    y += years
    average = (y/p)
    if p == 1 and gender == "M":
        oldest = years
        oldestname = name
    if gender == "M" and years > oldest:
        oldest = years
        oldestname = name
    if gender == "F" and years < 20:
        qwoman += 1
print(f"Average: {average:.2f}")
print(f"{oldestname} is the oldest man with {oldest} years")
print(f"We have {qwoman} girls under the twenty years")