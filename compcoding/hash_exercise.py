d={}
with open('nyc_weather.csv') as f:
    for line in f:
        words=line.split(',')
        try:
            d[words[0]]=int(words[1])
        except:
            pass
print(d['Jan 9'])
print(d['Jan 4'])
