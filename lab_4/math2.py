import math
height = int(input())
top = int(input())
lower = int(input())
area = ((top + lower)/2) * height
print(f'area of the trapezoid with height {height} and with bases {top, lower} is equal to {area}')