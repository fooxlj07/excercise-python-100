#example1
class Person(object):
    def __init__(self,age,name):
        self._name = name
        self._age = age
    
    @property
    def name(self):
        return self._name
    
    @property
    def age(self):
        return self._age
    
    @age.setter    
    def age(self, age):
        self._age = age

    @name.setter
    def name(self, name):
        self._name = name

    def play(self):
        print('%s is playing'% self._name)

def example1():
    p1 = Person(29,'Lily')
    print(p1._name, p1._age)
    p1.name = 'Ohlala'
    print(p1.name)

#example2
class Person2(object):
    # will fix the attribute of this class
    __slots__ = ('_name', '_age')

    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        if self._age <= 16:
            print('%s正在玩飞行棋.' % self._name)
        else:
            print('%s正在玩斗地主.' % self._name)


def example2():
    person = Person2('王大锤', 22)
    person.play()

from math import sqrt

class Triangle(object):

    def __init__(self,a,b,c):
        self._a = a
        self._b = b
        self._c = c
    
    # method belongs to class not object
    @staticmethod
    def is_valid(a,b,c):
        return a + b > c and b + c > a and a + c > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        half = self.perimeter()/2
        return sqrt(half * (half - self._a) * (half - self._b) * (half - self._c))

def example3():
    a,b,c = 12,24,21
    t = Triangle(a,b,c)
    if Triangle.is_valid(a,b,c):
        print(t.perimeter())
        print(t.area())

from time import sleep,localtime,time
import os
class Clock(object):

    def __init__(self, hour=0, minute=0, second=0):
        self._hour = hour
        self._minute = minute
        self._second = second
    
    @classmethod
    def now(cls):
        ctime = localtime(time())
        return cls(ctime.tm_hour,ctime.tm_min, ctime.tm_sec)

    def run(self):
        self._second += 1
        if self._second == 60:
            self._second = 0
            self._minute += 1
        if self._minute == 60:
            self._minute = 0
            self._hour += 1
        if self._hour == 24:
            self._hour = 0

def example4():
    c = Clock.now()
    print(Clock.now())
    while True:
        os.system('clear')
        print('%d:%d:%d'%(c._hour,c._minute,c._second))
        sleep(1)
        c.run()

# inherit
class Student(Person):

    def __init__(self,name,age,grade):
        super().__init__(age,name)
        self._grade = grade
    
    @property
    def grade(self):
        return self._grade
    
    @grade.setter
    def grade(self,grade):
        self.grade = grade 

    def play(self):
        print('Student %s is playing, he is at grade: %d'%(self._name, self._grade))

    def doing(self,action):
        print('Student %s is %s' % (self._name,action))

class Teacher(Person):
    def __init__(self,age,name,title):
        super().__init__(age,name)
        self._title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self,title):
        self._title = title
    
    def play(self):
        print('Teacher %s is playing' % self._name)

    def doing(self,action): 
        print('%s Teacher %s is %s'%(self._title,self.name,action))

def example5():
    s = Student('A',16,2)
    t = Teacher(29,'L','math')

    s.play()
    s.doing('studying')
    t.play()
    t.doing('teaching')

from abc import abstractmethod, ABCMeta

class Pet(object,metaclass=ABCMeta):
    def __init__(self, nickname):
        self._nickname = nickname
    
    @property
    def nickname(self):
        return self._nickname

    @nickname.setter
    def nickname(self,nickname):
        self._nickname = nickname

    @abstractmethod
    def make_voice(self):
        pass

class Cat(Pet):

    def make_voice(self):
        print('%s: meow meow...'%self._nickname)

class Dog(Pet):

    def make_voice(self):
        print('%s: woof woof'%self.nickname)   

def example6():
    cat = Cat('Mimi')
    dog = Dog('Izio')
    cat.make_voice()
    dog.make_voice()


from random import randint
from time import sleep

# abstract class
class Figther(object, metaclass = ABCMeta):
    __slots__ = ('_name','_hp','_attack_ticker','_total_count')

    def __init__(self, name, hp, total_count):
        self._name = name
        self._hp = hp
        self._total_count = total_count
        self._attack_ticker = total_count

    @property
    def name(self):
        return self._name
    
    @property
    def hp(self):
        return self._hp

    @property
    def attack_ticker(self):
        return self._attack_ticker

    @property 
    def total_count(self):
        return self._total_count

    @hp.setter
    def hp(self, hp):
        self._hp = hp if hp > 0 else 0 
   
    @attack_ticker.setter
    def attack_ticker(self, attack_ticker):
        self._attack_ticker = attack_ticker

    @abstractmethod
    def attack(self,other):
        pass
    
    def can_attack(self):
        return self._attack_ticker == 0 

class Monster(Figther):
    __slots__ = ('_name','_hp','_attack_ticker','_total_count')

    def __init__(self, name, hp, attack_ticker):
        super().__init__(name,hp,attack_ticker)

    def attack(self, other):
        print(self.name, 'MONSTER ATTACK')
        other._hp -= randint(10,20)
        if other._hp < 0:
            other._hp = 0
        return True

    def defend(self, other):
        other._hp -= randint(10,20)
        if other._hp < 0:
            other._hp = 0

    def __str__(self):
        return '~~~Monster %s~~~\n' % self._name + \
            'hp: %d \n' % self._hp  
   

def select_one_alive(others):
    alive = [other for other in others if other._hp > 0]
    index = randint(0,len(alive)-1)
    return others[index]

class Ultraman(Figther):
    __slots__ = ('_name','_hp','_attack_ticker','_mp','_total_count')

    def __init__(self, name, hp, total_count, mp):
        super().__init__(name,hp,total_count)
        self._mp = mp

    @property
    def mp(self):
        return self._mp
    
    @mp.setter
    def mp(self, mp):
        self._mp = mp

    def attack(self, others):
        print(self.name, 'ULTRAMAN ATTACK')
        monster = select_one_alive(others)
        monster.hp -= randint(15,25)
        if monster.hp < 0:
            monster.hp = 0
        return monster

    def magic_single_attack(self, others):
        monster = select_one_alive(others)
        if self._mp >= 30:
            print(self.name, 'ULTRAMAN SINGLE MAGIC ATTACK')
            self._mp -= 30
            monster.hp -= 50 
            if monster.hp < 0:
                monster.hp = 0
        else:
            self.attack(others)
        return monster

    def magic_multiple_attack(self, others):
        if self._mp >= 20:
            self._mp -= 20
            print(self.name, 'ULTRAMAN MULTIPLE MAGIC ATTACK')
            for monster in others:
                if monster.hp > 0:
                    monster.hp -= randint(15,25)
                if monster.hp < 0:
                    monster.hp = 0
        else:
            self.attack(others)


    def recover_magic(self):
        self._mp += randint(1,4)
    
    def __str__(self):
        return '~~~%s Ultamen~~~\n' % self._name + \
            'hp: %d \n' % self._hp + \
            'mp: %d \n' % self._mp 

def still_alive(others):
    if type(others) == object:
        return others.hp > 0
    else:
        for other in others:
            if other.hp > 0:
                return True
    return False

def time_counting(others):
    if not hasattr(others, '__iter__'):
        others.attack_ticker = others.attack_ticker - 1 if others.attack_ticker > 0 else others.total_count
    else:
        for other in others:
             other.attack_ticker = other.attack_ticker - 1 if other.attack_ticker > 0 else other.total_count

def display_info(m, u):
    print(u)
    for monster in m:
        print(monster, end='')

def excercise1():
    monster1 = Monster('A',100,2)
    monster2 = Monster('B', 120, 1)
    monster3 = Monster('C', 60, 1)
    monsters = [monster1,monster2,monster3]
    ultraman = Ultraman('Tiga', 200, 1, 100)
    round = 1
    while still_alive(monsters) and ultraman.hp > 0:
        sleep(1)
        os.system('clear')
        time_counting(monsters)
        time_counting(ultraman)
        monster = select_one_alive(monsters)
        print('IN ROUND %d'% round)
        strike = randint(1, 10)
        if monster.can_attack():
            monster.attack(ultraman)
        if ultraman.can_attack(): 
            if strike <= 6:
                attacked_monster = ultraman.attack(monsters) 
                attacked_monster.attack(ultraman)
            elif strike <= 8:
                ultraman.magic_multiple_attack(monsters)
            else:
                attacked_monster = ultraman.magic_single_attack(monsters)
                attacked_monster.attack(ultraman)
           

        display_info(monsters, ultraman)
        ultraman.recover_magic()
        round += 1
    if still_alive(monsters):
        print('The Monsters WIN')
    else:
        print('The Ultraman WIN')

# pocker
import random

class Card(object):
    __slots__ = ['_face','_suite']

    def __init__(self, suite, face):
        self._face = face
        self._suite = suite

    @property
    def face(self):
        return self._face 

    @property
    def suite(self):
        return self._suite

    def __str__(self):
        if self._face == 1:
            face_str = 'A'
        elif self._face == 11:
            face_str = 'J'
        elif self._face == 12:
            face_str = 'Q'
        elif self._face == 13:
            face_str = 'K'
        else:
            face_str = str(self._face)
        return '%s%s' % (self._suite, face_str)

    def __repr__(self):
        return self.__str__()
    
def get_key(self):
    return (self._suite, self._face)

# a suit of cards    
class Pocker(object):
    def __init__(self):
        self._cards = [Card(suite, face)
                        for face in range(1,14)
                        for suite in '♠♥♣♦']
        self._count = 0
    
    def suffle(self):
        self._count = 0
        random.shuffle(self._cards)

    def next(self):
        current = self._cards[self._count]
        self._count += 1
        return current

    def has_next(self):
        return self._count < len(self._cards) -1 

class Player(object):
    __slots__ = ['_name','_cards_in_hand']

    def __init__(self, name):
        self._name = name
        self._cards_in_hand = []

    @property
    def name(self):
        return self._name

    @property
    def cards_in_hand(self):
        return self._cards_in_hand

    def arrange(self):
        sorted(self._cards_in_hand, key=get_key)

    def get(self,card):
        self._cards_in_hand.append(card)

# just check
def excercise2():
    pocker = Pocker()
    players = [Player('A1'),Player('B2'),Player('C3'),Player('C4')]
    pocker.suffle()
    while pocker.has_next():
        for player in players:
            player.get(pocker.next())
    for player in players:
        print('\n Player %s:'%player.name)
        player.arrange()
        print(player.cards_in_hand, end = ',')

# Salary system
class Employee(object, metaclass=ABCMeta):
    
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    def get_salary(self):
        raise NotImplementedError

class Manager(Employee):
    def get_salary(self):
        return 15000.0

class Saler(Employee):
    def __init__(self, name, sale_volume):
        super().__init__(name)
        self._sale_volume = sale_volume
    
    def get_salary(self):
        return 1200.0 + self._sale_volume * 0.05

class Programmer(Employee):
    def __init__(self, name, working_hours):
        super().__init__(name)
        self._working_hours = working_hours

    def get_salary(self):
        return self._working_hours * 150

def excercise3():
    p = Programmer('Jing',40)
    s = Saler('Lee', 500000)
    m = Manager('Luo')
    print('Programmer %s get salary: %d'%(p.name, p.get_salary()))
    print('Manager %s get salary:%d'%(m.name, m.get_salary()))
    print('Saler %s get salary:%d'%(s.name, s.get_salary()))

if __name__ == '__main__':
    excercise3()

