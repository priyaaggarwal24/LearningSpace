import math

NAMES = ['John', 'Paul', 'Smith', 'David', 'George']
AGES = [25, 26, 27, 28, 29]

print(f"first two names are: {NAMES[0:2]}")
print(f"last three names are: {NAMES[2:]}")
print(f"Reversed list of names is {NAMES[::-1]}")
print(f"Minimum age is {min(AGES)}")
print(f"Maximum age is {max(AGES)}")
print(f"Average age is {math.floor(sum(AGES)/len(AGES))}")