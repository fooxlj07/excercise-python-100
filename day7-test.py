# example 2

def josh_circle():
    persons = [True] * 30
    index,number,count = 0,0,0
    while count < 15:
        if persons[index]:
            number += 1
            if number == 9:
                persons[index] = False
                count +=1
                number = 0
        index += 1
        index %= 30
    for person in persons:
        print('yes' if person else 'no',end='|') 
    print()


if __name__ == '__main__':
    josh_circle()