def count_a(n,s):
    count=0
    for c in s:
        count+=1 if c=='a' else 0
    count*=n//len(s)
    extra=n%len(s)
    for i in range(extra):
        count+=1 if s[i]=='a' else 0
    return count

s=input()
n=int(input())
print(count_a(n,s))
