n=int(input())
arr=[[0 for i in range(n)] for j in range(n)]
for _ in range(n):
    arr[_]=list(map(int,input().split()))
sum1,sum2=0,0
for i in range(n):
    sum1+=arr[i][i]
    sum2+=arr[i][n-i-1]
print(abs(sum1-sum2))
