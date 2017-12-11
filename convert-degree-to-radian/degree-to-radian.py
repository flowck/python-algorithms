# This program converts a degree number to a radian number

# Modules
from math import radians, degrees


# User input
givenNumber = input('Type a degree number: ')

# Convert into float to allow degree numbers like 5.5
x = float(givenNumber)

radian = radians(x)

print(radian)
