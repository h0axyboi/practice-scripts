
def isspecial(s):
    if len(s)%2!=0:
        newstr=s[0:len(s)//2]+s[len(s)//2+1:]
    else:
        newstr=s
    c=s[0]
    for ch in newstr:
        if ch!=c:
            return False
    return True

def substrCount(n, s):
    count=0
    for i in range(n):
        for j in range(n-i):
            if isspecial(s[j:j+i+1]):
                count+=1
    return count

if __name__ == '__main__':
    n=int(input())
    s=input()
    print(substrCount(n,s))
