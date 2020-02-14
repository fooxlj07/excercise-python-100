import time
import math


def main():
    testWriteJson()


def readLine():
    with open('test.txt', 'r', encoding='utf-8') as f:
        for line in f:
            print(line)
            time.sleep(0.05)
    with open('test.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        print(len(lines))
        print(lines)


def testWriteJson():
    import json
    d = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ]
    }

    try:
        with open('writed_files/t.json', 'w', encoding='utf-8') as f:
            json.dump(d, f)
    except Exception as e:
        print(str(e))


def testWriteTXT():
    def is_prime(n: int) -> bool:
        for j in range(2, int(math.sqrt(n)) + 1):
            if n % j == 0:
                return False
        return True if n != 1 else False

    a_file = open('a.txt', 'w', encoding='utf-8')
    b_file = open('b.txt', 'w', encoding='utf-8')
    c_file = open('c.txt', 'w', encoding='utf-8')
    try:
        for i in range(1, 10000):
            if is_prime(i):
                if i < 100:
                    a_file.write(str(i) + '\n')
                elif i < 1000:
                    b_file.write(str(i) + '\n')
                else:
                    c_file.write(str(i) + '\n')
    except IOError as e:
        print(e)
    finally:
        a_file.close()
        b_file.close()
        c_file.close()


def read1(path: str, encoding: str = 'utf-8'):
    f = None
    try:
        f = open(path, 'r', encoding=encoding)
        print(f.read())
        f.close()
    except FileNotFoundError as e:
        print("can't find the file", str(e))
    except LookupError as e:
        print("unknown encoding", str(e))
    except UnicodeDecodeError as e:
        print("errors during the read", str(e))
    finally:
        if f:
            f.close()


if __name__ == '__main__':
    main()
