NAMES = ['John', 'Paul', 'Smith', 'David', 'George']
AGES = [25, 26, 27, 28, 29]

print("Iteration using while loop")
i = 0
while i < len(NAMES):
    print(f"{i} {NAMES[i]}'s age is: {AGES[i]}")
    i += 1

print("Iteration using for in loop")
for name in NAMES:
    print(name)

print("Iteration using for with zip")
for name, age in zip(NAMES, AGES):
    print(f"{name}'s age is {age}")

print("Iteration using for with enumerator")
for i, name in enumerate(NAMES):
    print(f"{i} {name}")

print("Reversed list iteration using for with enumerator")
for i, name in enumerate(reversed(NAMES)):
    print(f"{i} {name}")

print("print range of numbers")
for i in range(3, 6, 2):
    print(i)