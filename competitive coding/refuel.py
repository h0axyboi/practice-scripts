print('This program calculates the minimum number of refuels needed')
D,d=map(int,input('Enter the total distance and the mileage of the car on a full tank as two space separated integers').split())
stations=list(map(int,input('Enter the coordinates of the refuel hubs as space separated integers').split()))
stations.insert(0,0)
stations.append(D)
res,currloc,lastloc=0,0,0

while currloc<=len(stations)-2:
    lastloc=currloc
    while currloc<=len(stations)-2 and stations[currloc+1]-stations[lastloc]<=d:
        currloc+=1
    if currloc==lastloc:
        print('impossible')
        exit()
    if currloc<=len(stations)-2:
        res+=1
print(res)
