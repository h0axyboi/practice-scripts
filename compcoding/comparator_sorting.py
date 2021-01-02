class People:
    def __init__(self,name,score):
        self.name=name
        self.score=int(score)

arr=[]
n=int(input())
for i in range(n):
    name,score=input().split()
    player=People(name,score)
    arr.append(player)
arr.sort(key=lambda x: x.score, reverse=True)
temp=[]
new_arr=[]
for i in range(len(arr)):
    if len(temp)==0:
        temp.append(arr[i])
        continue
    if temp[-1].score==arr[i].score:
        temp.append(arr[i])
    else:
        temp.sort(key=lambda x:x.name)
        new_arr=new_arr+temp
        temp=[arr[i]]
temp.sort(key=lambda x:x.name)
new_arr=new_arr+temp
for thing in new_arr:
    print(thing.name,thing.score)
