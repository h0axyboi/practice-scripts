def valid_or_not(s):
    d={}
    for c in s:
        d[c]=d.get(c,0)+1
    freq={}
    for key,value in d.items():
        freq[value]=freq.get(value,0)+1
    if len(freq)==1:
        return 'YES'
    if len(freq)==2:
        x=list(freq.keys())
        y=list(freq.values())
        a=x[0]
        b=x[1]
        c=y[0]
        d=y[1]
        if (a==1 and c==1) or (b==1 and d==1):
            return 'YES'
        if (c==1 and a==b+1) or (d==1 and b==a+1):
            return 'YES'
    return 'NO'

print(valid_or_not(input()))
