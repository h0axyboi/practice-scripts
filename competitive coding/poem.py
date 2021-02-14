d=dict()
with open('poem.txt') as f:
    for line in f:
        words=line.rstrip().split()
        for word in words:
            d[word]=d.get(word,0)+1
print(d)
