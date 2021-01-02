def isOrdered(num,maxi):
    if int(str(num)+str(maxi))>=int(str(maxi)+str(num)):
        return True
    return False

def findsalary(n,numbers):
    salarystr=''
    while len(numbers)>0:
        maxi=numbers[0]
        for num in numbers:
            if isOrdered(num,maxi):
                maxi=num
        salarystr+=str(maxi)
        del numbers[numbers.index(maxi)]
    return int(salarystr)

print('This program calculates the maximum salary that can be ordered from integers provided')
n=int(input('Enter the number of integers: '))
numbers=list(map(int,input('Enter the different space separated integers: ').split()))
salarymax=findsalary(n,numbers)
print(salarymax)
