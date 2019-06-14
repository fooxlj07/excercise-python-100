import math

def triple(i,j,k):
    return math.pow(i, 3) + math.pow(j, 3) + math.pow(k,3)

def threeDigits(i,j,k):
    return i * math.pow(10,2) + j * 10 + k

print("the narcissistic number are:")
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            if triple(i,j,k)== threeDigits(i,j,k):
                print(threeDigits(i,j,k))

k = int(input())
print("the perfect number less than %d are"%(k))
for i in range(1,k):
    sum = 0
    for j in range(1,int(i/2+1)):
        if i%j == 0:
            sum += j
    if sum == i:
        print(i)

print("use 100 rmb to buy chicken")
for i in range(0,20):
    for j in range(0,33):
        for k in range(0,300):
            sum = i * 5 + j * 3 + k * 1/3 
            if sum == 100 and i + j + k ==100:
                print("cock: %d, hen: %d, chick: %d"%(i, j ,k))


def fibo(n):
    if n == 1 or n == 2:
        return 1
    return fibo(n-1)+fibo(n-2)
n = int(input())
print(fibo(n))

from random import randint
dice1 = randint(1,6)
dice2 = randint(1,6)
sum = dice1 + dice2
print("the dice are %d, %d"%(dice1,dice2))
if sum == 7 or sum == 11:
    print("the dice are %d, %d is win "%(dice1,dice2),True) 
elif sum ==2 or sum == 3 or sum == 12:
    print("the dice are %d, %d is win "%(dice1,dice2),False) 
sumLater = 0 
while sumLater != sum and sumLater != 7:
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    sumLater = dice1 + dice2
    print("the dice are %d, %d"%(dice1,dice2))
if sumLater == sum:
    print("the dice are %d, %d, first time is %d is win "%(dice1,dice2,sum),True) 
else:
    print("the dice are %d, %d is win "%(dice1,dice2),False) 