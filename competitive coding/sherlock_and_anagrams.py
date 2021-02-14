def sherlockAndAnagrams(s):
    d={}
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            d[''.join(sorted(s[i:j]))]=d.get(''.join(sorted(s[i:j])),0)+1
    count=0
    for thing in d:
        count+=(d[thing]*(d[thing]-1))//2
    return count

if __name__=='__main__':
    n=int(input())
    for _ in range(n):
        print(sherlockAndAnagrams(input()))
