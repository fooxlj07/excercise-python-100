from module1 import foo
from module2 import foo
import utils

foo()
# test __name__
# if __name__ == '__main__':
#     print("excuting test.py")

# # excercise 1
# x = int(input('x = '))
# y = int(input('y = '))
# print(utils.gcd(x,y))
# print(utils.lcm(x,y))

## excercise 2
# k = int(input())
# print('the number inputed is a palindrome number by func isPalindrome:',utils.isPalindrome(k))
# print('the number inputed is a palindrome number by func is_palindrome:',utils.is_palindrome(k))

# # excercise 3
# print('the input number is a prime number:',utils.is_prime(int(input('x = '))))

# # ecsercise 3
# k = int(input('k = '))
# print('the input numner is a prime and a palindrome number:',\
#      utils.is_palindrome(k) and utils.is_prime(k))

def fooo():
    global a
    a = 200
    b = 111
    def bar():
        nonlocal b
        b = 123 
        print(b)
    bar()
    print(b)  # 200


if __name__ == '__main__':
    a = 100
    fooo()
    print(a)  # 200