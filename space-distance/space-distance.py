# Algorithms:

# Build a program that read a spacial coordinates of two points: P1(x1, y1) and
# P2(x2, y2). Then calculate the distance between of two points from this formule: 
# d = √(x2-x1)^2 + (y2-y1)^2

# Import modules
from math import sqrt

#     x  y
p1 = []
p2 = []

# Insert values in the first coordinates
print('P1 coordinate values')

# Convert the input values into int and then insert into array
p1.insert(0, int(input('Insert x1 number: ')))
p1.insert(1, int(input('Insert y1 number: ')))

print('\n \n P2 coordinate values \n ')

# Convert the input values into int and then insert into array
p2.insert(0, int(input('Insert x2 number: ')))
p2.insert(1, int(input('Insert y2 number: ')))

operation = pow((p2[0] - p1[0]), 2) + pow((p2[1] - p1[1]), 2)

# Caculate the distance
d = sqrt(operation)

print(d)