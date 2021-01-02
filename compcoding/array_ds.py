e=[2200,2350,2600,2130,2000]

print('The amount of money spent extra in Feb compared to Jan is: Rs',e[1]-e[0])
print('total expense in the first quarter is: Rs',e[0]+e[1]+e[2])
print('Did i spend exactly 2000 in any of the months?',2000 in e)
e.append(1980)
e[3]=e[3]-200
print(e)

heros=['spider man','thor','hulk','iron man','captain america']
print('Length of the list:',len(heros))
heros.append('black panther')
print(heros)
heros.remove('black panther')
heros.insert(3,'black panther')
print(heros)
heros[1:3]=['doctor strange']
print(heros)
heros.sort()
print(heros)

max_num=int(input())
odd_list=[]
for i in range(1,max_num+1,2):
    odd_list.append(i)
print(odd_list)
