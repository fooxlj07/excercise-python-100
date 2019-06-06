#Example1

sum = 0

for x in range(2, 101, 2):
    sum+=x
print(sum)


#Example2
from random import randint

num = randint(1,100)
guess = 0
count = 0
while  (guess != num and count <= 7):
    guess = int(input('please guess a number:'))
    if guess < num:
        print('the guessed number is smaller')
    elif guess > num:
        print('the guessed number is bigger')
    else:
        print('You guessed correctly！')
        break
    count+=1
print('has tried %d times'%(count))

# Example 3
for i in range(1, 10):
    for j in range(1,i+1):
        print("%d * %d = %d"% (i,j,i*j), end='\t')
    print()

# Excercise 1
from math import sqrt

num = int(input('please input a number:'))
end = int(sqrt(num))
for x in range(2, end+1):
    if num / x == 0:
        print(False,'it can be divide by ',x)
        break
print(True) 

# Excercise1
x = int(input('please input the first number:'))
y = int(input('please input the seconde number:'))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print(factor)
        print(x * y / factor)
        break

# Excercise 3

row = int(input('please input the row:'))
for x in range(row+1):
    s = ''
    for i in range(x):
        s+='*'
    print(s)

for i in range(row+1):
    s = ''
    for _ in range(row-i):
        s += ' ' 
    for _ in range(i):
        s += '*'
    print(s)

for i in range(row+1):
    s = ''
    for _ in range(row-i):
        s += ' '
    for _ in range(2*i-1):
        s += '*'
    print(s)
