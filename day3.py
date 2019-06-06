# Excercise1

v = float(input('please input the value:'))
unit = str(input('please input the unit:'))

if unit == 'in':
    print('%.2f in is %.2f cm' % (v, v*2.54))
elif  unit == 'cm':
    print('%.2f cm is %.2f in' % (v, v/2.54))
else:
    print('invalid input of unit')

# Excercise2

from random import randint

face = randint(1,6)
if face == 1:
    result = 'sing a song'
elif face == 2:
    result = 'dance'
elif face == 3:
    result = 'bark'
elif face == 4:
    result = 'swim'
elif face == 5:
    result = 'sleep'
else:
    result = 'play video game'
print(result)

# Excercise3

score = randint(40, 100)

if score>=90:
    result = 'A'
elif score >=80 and score < 90:
    result = 'B'
elif score >=70 and score <80:
    result = 'C'
elif score >=60 and score < 70:
    result = 'D'
else:
    result = 'E'
print('the grade is :', result)

#excersice4
import math
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a+b >c and a+c > b and b+c > a:
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('area is %.2f'%(area))
else:
    print('can\'t be a triangle')
