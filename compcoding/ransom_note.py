def runthing():
    m,n=map(int,input().split())
    mag_list=list(input().split())
    ran_list=list(input().split())
    mag,ran={},{}
    for thing in mag_list:
        mag[thing]=mag.get(thing,0)+1
    for thing in ran_list:
        if thing not in mag or mag[thing]==0:
            return False
        mag[thing]-=1
    return True

if __name__=='__main__':
    if runthing():
        print('Yes')
    else:
        print('No')
