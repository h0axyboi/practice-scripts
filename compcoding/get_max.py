def getmax(a,b,c,d,e):
    maxi=0
    costp1,costp2,costp3,costp4=0,0,0,0
    x1,x2,x3,x4=0,0,0,0
    rem=0
    remdash=0
    maxidash=0
    x1dash,x2dash,x3dash,x4dash=0,0,0,0
    for i in range(4):
        costp1+=a[0][i]*b[i]
        costp2+=a[1][i]*b[i]
        costp3+=a[2][i]*b[i]
        costp4+=a[3][i]*b[i]
    costs=[costp1,costp2,costp3,costp4]
    print(costs)
    for i in range(5,36):
        for j in range(5,36):
            for k in range(5,36):
                for l in range(5,36):
                    if costs[0]*i+costs[1]*j+costs[2]*k+costs[3]*l>20000: continue
                    rev_product=(1-d[0])*i*(c[0]-costs[0])+(1-d[1])*j*(c[1]-costs[1])+(1-d[2])*k*(c[2]-costs[2])+(1-d[3])*l*(c[3]-costs[3])
                    remaining=20000-costs[0]*i-costs[1]*j-costs[2]*k-costs[3]*l
                    rev_project=remaining*e
                    if i==15 and j==34 and k==5 and l==12:
                        remdash=remaining
                        x1dash=i
                        x2dash=j
                        x3dash=k
                        x4dash=l
                        maxidash=rev_product+rev_project
                    if rev_product+rev_project>maxi:
                        rem=remaining
                        x1=i
                        x2=j
                        x3=k
                        x4=l
                        maxi=rev_product+rev_project

    return maxi,x1,x2,x3,x4,rem,maxidash,x1dash,x2dash,x3dash,x4dash,remdash


res_needed=[[10,3,5,4],[2,10,7,3],[3,6,10,2],[3,3,2,10]]
res_prices=[[19,12,13,15],[16,18,9,21],[14,16,12,19],[18,15,13,17]]
pro_prices=[[530,450,410,400],[500,480,450,450],[520,470,430,410],[550,475,440,420]]
duty=[[0.08,0.09,0.075,0.05],[0.05,0.15,0.15,0.15],[7.5,0.18,0.1,0.05],[0.13,0.135,0.12,0.075]]
project_return=[0.08,0.165,0.18,0.09]
africa,w1,w2,w3,w4,rem1,f,g,h,j,k,l=getmax(res_needed.copy(),res_prices[0].copy(),pro_prices[0].copy(),duty[0].copy(),project_return[0])
print(africa,w1,w2,w3,w4,rem1,f,g,h,j,k,l)
#europe,x1,x2,x3,x4,rem2=getmax(res_needed.copy(),res_prices[1].copy(),pro_prices[1].copy(),duty[1].copy(),project_return[1])
#print(europe,x1,x2,x3,x4,rem2)
#la,y1,y2,y3,y4,rem3=getmax(res_needed.copy(),res_prices[2].copy(),pro_prices[2].copy(),duty[2].copy(),project_return[2])
#print(la,y1,y2,y3,y4,rem3)
#na,z1,z2,z3,z4,rem4=getmax(res_needed.copy(),res_prices[3].copy(),pro_prices[3].copy(),duty[3].copy(),project_return[3])
#print(na,z1,z2,z3,z4,rem4)
