t=int(input())
for _ in range(t):
    d=dict()
    n=int(input())
    arr=list(map(int,input().split()))
    for num in arr:
        d[num]=d.get(num,0)+1
    freqd=dict()
    for key,value in d.items():
        freqd[value]=freqd.get(value,0)+1
    maxfreqfreq=max(freqd.values())
    answers=[k for k,v in freqd.items() if v==maxfreqfreq]
    print(min(answers))
