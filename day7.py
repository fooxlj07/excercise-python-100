
def fibo(max):
    a,b = 0, 1
    for _ in range(0,max+1):
        yield b
        a, b =b, a+b
    return 'done'

# strings cab be treat as an array
def test_str():
    str1 = "hello, world"
    str2 = '我叫fooxlj'
    str3 = 'abc \t'

    print(str1.center(20,'*')) 
    # 将字符串以指定的宽度靠右放置左侧填充指定的字符 
    print(str1.rjust(20,'*'))
    print(str1.ljust(20,'*'))

    print(str2)
    print(str2.encode(encoding='utf-8', errors='strict'))
    #Encode S using the codec registered for encoding

    print(str3,str3.expandtabs(tabsize=12),str2)
    #Return a copy of S where all tab characters are expanded using spaces. If tabsize is not given, a tab size of 8 characters is assumed.

    print(str1.find('l'))
    print(str1.find('shit'))

    print(str1.index('l'))
    #print(str1.index('aa'))
    # 与find类似但找不到子串时会引发异常

    print(str1.isdigit())
    print(str2.isdigit()) 
  
   # 检查字符串是否以字母构成
    print(str2.isalpha()) 
    # 检查字符串是否以数字和字母构成

    print(str2.isalnum()) 
    str3 = '  jackfrued@126.com '
    print(str3)
    # 获得字符串修剪左右两侧空格的拷贝
    print(str3.strip())

def test_arr():
    # ARRAY
    fruits = ['grape', 'apple', 'strawberry', 'waxberry']
    fruits += ['pitaya', 'pear', 'mango']
    
    #取值
    print(fruits)
    print(fruits[-3:-1])
    print(fruits[::-1]) #倒序
    print(fruits[::-3]) #倒序，取每隔2个的值
   
    print('SORT')
    #sort 
    print(fruits)
    print(sorted(fruits))
    # sorted函数返回列表排序后的拷贝不会修改传入的列表
    # 函数的设计就应该像sorted函数一样尽可能不产生副作用 
    print(sorted(fruits,reverse = True))
    print(sorted(fruits,key=len))
    print(sorted(fruits,key=len,reverse=True))
    print(fruits)

    #Construct Array by Function
    import sys

    arr = [1,2,3,4,5,6,7,8,9,10]
    f = [x * 2 for x in range(1,11)]
    print(f)
    # 用这种语法创建列表之后元素已经准备就绪所以需要耗费较多的内存空间, 如下
    print(sys.getsizeof(f))  
    print(sys.getsizeof(arr))

    f = [x ** 2 for x in range(1, 1000)]
    print(sys.getsizeof(f))  # 查看对象占用内存的字节数
    print(f,'first')
    
def test_generator():
    import sys
    # 请注意下面的代码创建的不是一个列表而是一个生成器对象
    # 通过生成器可以获取到数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部的运算得到数据(需要花费额外的时间)
    
    f = (x * 2 for x in range(1, 11))
    print(sys.getsizeof(f))  # 相比生成式生成器不占用存储数据的空间
    print(f,'second')
    print(next(f))
    print(next(f))
    print(next(f))
    for val in f:
        print(val)
    a = fibo(10)
    print(fibo(10))
    print(a.__next__())
    print(a.__next__())
    print('do something else')
    print(a.__next__())
    print('start for loop')
    for val in a:
        print(val)

    b = fibo(6)
    while True:
        try:
            print('generator b',b.__next__())
        except StopIteration as e:
            print("生成器返回值：",e.value)
            break
    
    c = fibo(7)
    print(list(c))

from ctypes import *
# for tuple
def test_tuple():
    import sys
    t = ('abc', 24, '狐狸' , True)
    print(t)
    t = ('土豆', '茄子', '狐狸' , True)
    print(t)
    arr = ['土豆', '茄子', '狐狸' , True]
    print(sys.getsizeof(t),sys.getsizeof(arr))

import time
def consumer(name):
    print("%s 准备学习啦!" %name)
    while True:
       lesson = yield
 
       print("开始[%s]了,[%s]老师来讲课了!" %(lesson,name))
 
 
def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    next(c2)
    print("同学们开始上课 了!")
    for i in range(3):
        time.sleep(1)
        print("到了两个同学!")
        c.send(i)
        c2.send(i)

def test_set():
    set1 = {1,2,2,3,5,6}
    set2 = {2,4,7,9,1,0,5}
    print(set1)
    print(set2)
    print('Length of set1',len(set1),'Length of set2',len(set2))
    set1.add(11)
    print(set1)
    set2.update({1,66})
    print(set2)
    set2.remove(66)
    print(set2)
    # set2.remove(66)
    set2.discard(66)
    print(set1)
    print(set2)
    print(set1 & set2)
    print(set1 | set2)
    print(set2 ^ set1)
    print(set2 - set1)
    set3 = set(range(0,10))
    print(set3 >= set1)
    print(set3 >= set2)

def test_dict():
    scores = {'骆昊': 95, '白元芳': 78, '狄仁杰': 82, 666: 66}
    print(scores)
    for elem in scores:
        print(elem)
    scores['jack'] = 66
    scores[777] = 77
    scores.update(Lucy=121,Lily=111)
    print(scores.pop(666,66))
    print(scores.popitem())
    print(scores.get('Lucy',55))
    print(scores.get('Lee',120))
    print(scores)
    if 'Lucy' in scores:
        print('Lucy')
    print(scores['lucy'])

def horse_race_lamp():
    import os
    import time
    content = 'I love Lol '
    while True:
        os.system('clear') # command input in commander
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[:1]
        
def generate_captcha():
    import random
    import string
    l = int(input('please input the length of capthca: '))
    num = string.ascii_letters + string.digits
    print("".join(random.sample(num,l))) 

def generate_captcha2():
    import random
    import string
    l = int(input('please input the length of capthca: '))
    num = string.ascii_letters + string.digits
    code = ""
    for _ in range(l):
        code += num[random.randint(0,len(num)-1)]
    print(code)
    
def get_file_suffix1(filename):
    arr = filename.split('.',-1)
    print(arr)
    if len(arr) > 0:
        return arr[len(arr)-1]
    else:
        return ''

def get_file_suffix2(filename):
    index = filename.rfind('.')
    if index > 0 and index+1 < len(filename)-1:
        return filename[index+1:]
    else:
        return ''

def get_maxes1(arr):
    if len(arr) < 2:
        return ()
    arrSorted = sorted(arr)
    return (arrSorted[len(arr)-2],arrSorted[len(arr)-1])

def get_maxes2(arr):
    m1, m2 = (arr[0], arr[1]) if arr[0] < arr[1] else (arr[1], arr[0])
    for i in range(len(arr)):
        if arr[i] > m2:
            m1 = m2
            m2 = arr[i]
        elif arr[i] > m1:
            m1 = arr[i]
    return m1,m2

def is_leap_year(year):
    return year % 4 == 0 and year % 100 !=0 or year % 400 == 0

def which_day(year, month, day):
    d = 0
    m = [i for i in range(1,13)]
    if is_leap_year(year):
        m[2] = 29
    
    small_month_set = {4,6,9,10}
    for i in small_month_set:
        m[i] = 30
    for i in set(range(1,13))-small_month_set:
        m[i] = 31
    for mon in range(1,month):
        d += m[mon]
    return d + day

def yang_hui_triangle(num):
    yh = [[]] * num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col == 0 or col == row:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col] + yh[row - 1][col - 1]
        print('\t'.join(map(str,yh[row])))


if __name__ == '__main__':
    # producer('foox')
    # consumer('ohlala')
    # test_set()
    # test_dict()
    # horse_race_lamp()
    # generate_captcha2()
    # print(get_file_suffix2('file.li.doc'))
    # print(get_maxes2(['grape', 'apple', 'strawberry', 'waxberry']))
    # print(which_day(1990,3,7))
    # print(yang_hui_triangle(int(input('Yang Hui Level= '))))
    numbers = [1,5,7,9]
    numbers[1:3] = [2,3,4]
    print(numbers)