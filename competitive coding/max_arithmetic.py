def minimize(ma1,mi1,ma2,mi2,op):
    if op=='+':
        return mi1+mi2
    elif op=='-':
        return mi1-ma2
    elif op=='*':
        return mi1*mi2

def maximize(ma1,mi1,ma2,mi2,op):
    if op=='+':
        return ma1+ma2
    elif op=='-':
        return ma1-mi2
    elif op=='*':
        return ma1*ma2

def get_max(nums,oper,i,j,maxi,mini):
    if i==j:
        return nums[i]
    ma=maximize(maxi[i][i],mini[i][i],maxi[i+1][j],mini[i+1][j],oper[i])
    for x in range(i,j):
         ma=max(ma,maximize(maxi[i][x],mini[i][x],maxi[x+1][j],mini[x+1][j],oper[x]))
    return ma

def get_min(nums,oper,i,j,maxi,mini):
    if i==j:
        return nums[i]
    mi=minimize(maxi[i][i],mini[i][i],maxi[i+1][j],mini[i+1][j],oper[i])
    for x in range(i,j):
        mi=min(mi,minimize(maxi[i][x],mini[i][x],maxi[x+1][j],mini[x+1][j],oper[x]))
    return mi

def max_arith(nums,oper):
    maxi=[[0 for i in range(len(nums))] for j in range(len(nums))]
    mini=[[0 for i in range(len(nums))] for j in range(len(nums))]
    for s in range(len(nums)):
        for i in range(len(nums)-s):
            j=i+s
            maxi[i][j]=get_max(nums,oper,i,j,maxi,mini)
            mini[i][j]=get_min(nums,oper,i,j,maxi,mini)
    return maxi[0][len(nums)-1]

if __name__=='__main__':
    inp=input()
    nums=[]
    oper=[]
    for i in range(len(inp)):
        if i%2==0:
            nums.append(int(inp[i]))
        else:
            oper.append(inp[i])
    print(max_arith(nums,oper))
