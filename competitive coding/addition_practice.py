import random

def practice_addition(n):
    a=[59,68,77,96,84,32,17,69,81,38]
    b=[48,54,67,89,56,73,88,24,47,96]
    count=0
    for i in range(n):
        q1=random.choice(a)
        q2=random.choice(b)
        print('{}+{}'.format(q1,q2))
        answer_str=input()
        try:
            answer_int=int(answer_str)
        except:
            print('Game over!')
            return
        if answer_int==q1+q2:
            count+=1
    print('Your score is: {}/{}'.format(count,n))

def practise_10():
    a=[59,68,77,96,84,32,17,69,81,38,48,54,67,89,56,73,88,24,47,96]
    count=0
    for _ in range(10):
        x=random.choice(a)
        count+=x
        print(x)
    answer_str=input()
    try:
        answer_int=int(answer_str)
    except:
        print('Wrong answer!')
        return
    print('Right one!' if answer_int==count else 'Wrong Answer!')
    return

if __name__=='__main__':
    n=input('Enter a number to get that many addition problems to solve: ')
    practice_addition(int(n))
    print('Add these ten numbers too, to wind up:')
    practise_10()
