n,k=map(int,input().split())
sen_arr=list(map(int, input().split()))
stack,fear=[],1
for i in range(n):
    while(stack and stack[-1][0]>sen_arr[i]):
        fear=(fear*(i-stack[-1][1]+1))%1000000007
        stack.pop()
    stack.append([sen_arr[i],i])
print(fear)
