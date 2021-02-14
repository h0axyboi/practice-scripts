import random
def generate_questions(n):
    for _ in range(n):
        x=random.randint(11,100)
        print(x)
        inp=int(input())
        if inp==x**2:
            continue
        else:
            print('Wrong! the right answer is: {}'.format(x**2))

n=int(input())
generate_questions(n)
