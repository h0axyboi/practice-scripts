def count_valleys(n,inp):
    alt=0
    count=0
    for ch in inp:
        x=alt
        alt+=1 if ch=='U' else -1
        if x==0 and alt==-1:
            count+=1
    return count

n=int(input())
inp=input()
print(count_valleys(n,inp))
