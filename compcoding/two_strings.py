for _ in range(int(input())):
    s1=input()
    s2=input()
    k=0
    for c in s1:
        if c in s2:
            print('YES')
            k=1
            break
    if k==0: print('NO')
