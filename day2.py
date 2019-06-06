
# Exercise1

# F = 1.8C +32
f = float(input('please input the degree fahenheit:'))
c = (f - 32)/1.8
print('the dgree Celsius is ',c)

# Exercise2

import math

radius = float(input('please input the radius:'))
perimeter = 2 * math.pi * radius
area = math.pi * (radius**2)
print('the perimeter is %.2f'% perimeter)
print('the area is %.2f' % area)

# Exercise3

year = float(input('please input a year:'))
print(year%4 == 0 and year % 100 !=0 or year % 400 == 0)