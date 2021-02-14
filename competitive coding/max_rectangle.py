n = int(input())
rec = []
rec.append((0,0))
for _ in range(n):
    s,e = map(int, input().split())
    if rec[-1][0] != s:
        rec.append((s,500))
    rec.append((s,e))
rec.append((100000,0))
print(rec)
rec.sort(key=lambda x:(x[0],x[1]))
print(rec)
n = len(rec)
right = [0]*n
left = [0]*n

stack = []

for i in range(n):
    while stack != []:
        ind,x,y = stack[-1]
        if rec[i][1] < y:
            right[ind] = rec[i][0]
            stack.pop()
        else:
            break
    stack.append((i,rec[i][0],rec[i][1]))
stack = []
for i in range(n-1,-1,-1):
    while stack != []:
        ind,x,y = stack[-1]
        if rec[i][1] < y:
            left[ind] = rec[i][0]
            stack.pop()
        else:
            break
    stack.append((i,rec[i][0],rec[i][1]))


# print(rec)
# print(right)
# print(left)

maxi = 0

for i in range(n):
    area = rec[i][1]*(right[i]-left[i])
    maxi = max(maxi,area)

print(maxi)
