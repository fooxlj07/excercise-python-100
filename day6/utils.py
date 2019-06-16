import math

def gcd(x, y):
    (x, y) = (y,x) if x > y else (x, y)
    max = 0
    for i in range(1,x+1):
        if x % i == 0 and y % i == 0 and i > max:
            max = i
    return max

def lcm(x,y):
    return x * y // gcd(x,y)

def isPalindrome(x):
    if type(x) != int:
        return False
    y = str(x)
    i, j = len(y)-1,0
    while i > j:
        if y[i] != y[j]:
            return False
        i = i-1
        j = j+1
    return True
        
def is_palindrome(num):
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

def is_prime(x):
    for i in range(2,int(math.sqrt(x))):
        if x % i == 0:
            return False
    return True