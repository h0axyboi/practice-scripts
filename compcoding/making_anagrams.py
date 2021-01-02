str1=input()
str2=input()
d1,d2={},{}
for c in str1:
    d1[c]=d1.get(c,0)+1
for c in str2:
    d2[c]=d2.get(c,0)+1
count=0
x=list(d1.items())
for key,value in x:
    if key in d2:
        count+=abs(d2[key]-value)
        del d2[key]
    else:
        count+=value
    del d1[key]
count+=sum(d2.values())
print(count)
