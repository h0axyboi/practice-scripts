import csv
import numpy as np
from sklearn.preprocessing import normalize

def getarray(s):
    file=open(s,newline='')
    reader=csv.reader(file)
    return [row for row in reader]

def stretch(x):
    m,n=len(x),len(x[0])
    new_arr=[[0 for i in range(m)] for j in range(n)]
    for i in range(m):
        for j in range(n):
            new_arr[j][i]=float(x[i][j])
    mins=[min(thing) for thing in new_arr]
    maxs=[max(thing) for thing in new_arr]
    stretched_new=[[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            if maxs[i]==mins[i]:
                stretched_new[i][j]=new_arr[i][j]
                continue
            stretched_new[i][j]=(new_arr[i][j]-mins[i])/(maxs[i]-mins[i])*10
    return stretched_new

def get_mean(a,b,c):
    mean_arr=[[0 for i in range(len(a[0]))] for j in range(len(a))]
    m,n=len(a[0]),len(a)
    for i in range(n):
        for j in range(m):
            mean_arr[i][j]=(a[i][j]+b[i][j]+c[i][j])/3
    return mean_arr

def get_weighted(arr,w):
    ans=[0 for i in range(len(arr[0]))]
    m,n=len(arr[0]),len(arr)
    sum_w=sum(w)
    for i in range(n):
        w[i]=w[i]/sum_w
    for j in range(m):
        for i in range(n):
            ans[j]+=w[i]*arr[i][j]
    return ans

if __name__=='__main__':
    projects=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\project_details.csv')
    g1a=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g1a.csv')
    g1b=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g1b.csv')
    g1c=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g1c.csv')
    g2a=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g2a.csv')
    g2b=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g2b.csv')
    g2c=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g2c.csv')
    g3a=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g3a.csv')
    g3b=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g3b.csv')
    g3c=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g3c.csv')
    g4a=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g4a.csv')
    g4b=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g4b.csv')
    g4c=getarray(r'C:\Users\Sabari\Desktop\python scripts\CRC scoring\scores\g4c.csv')
    g1a_s=stretch(g1a)
    g1b_s=stretch(g1b)
    g1c_s=stretch(g1c)
    g2a_s=stretch(g2a)
    g2b_s=stretch(g2b)
    g2c_s=stretch(g2c)
    g3a_s=stretch(g3a)
    g3b_s=stretch(g3b)
    g3c_s=stretch(g3c)
    g4a_s=stretch(g4a)
    g4b_s=stretch(g4b)
    g4c_s=stretch(g4c)
    g1_table=get_mean(g1a_s,g1b_s,g1c_s)
    g2_table=get_mean(g2a_s,g2b_s,g2c_s)
    g3_table=get_mean(g3a_s,g3b_s,g3c_s)
    g4_table=get_mean(g4a_s,g4b_s,g4c_s)
    weights=[90,70,25,75,40,60]
    g1=get_weighted(g1_table,weights)
    g2=get_weighted(g2_table,weights)
    g3=get_weighted(g3_table,weights)
    g4=get_weighted(g4_table,weights)
    g1_normal=list(normalize([g1],norm='max')[0])
    g2_normal=list(normalize([g2],norm='max')[0])
    g3_normal=list(normalize([g3],norm='max')[0])
    g4_normal=list(normalize([g4],norm='max')[0])
    complete_arr_normal=g1_normal+g2_normal+g3_normal+g4_normal
    s=np.array(complete_arr_normal)
    ranking=list(np.argsort(s))
    ranking.reverse()
    for i in ranking:
        print(projects[i])
