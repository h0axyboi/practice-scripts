def get_alt(s):
    count=0
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
    return count

n=int(input())
for _ in range(n):
    print(get_alt(input()))
