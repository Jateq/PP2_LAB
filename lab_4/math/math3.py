from math import tan
from math import pi
number_of_sides = int(input())
length_of_side = int(input())
tangent = tan(pi/4)
area = (number_of_sides * length_of_side)/(4*tangent)
print(int(area))