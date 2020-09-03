def do_Y():
    space=[' ']*9
    for i in range(9):
        space[i]=F[i]
    for i in range(9):
        F[i]=R[i]
    for i in range(9):
        R[i]=B[i]
    for i in range(9):
        B[i]=L[i]
    for i in range(9):
        L[i]=space[i]
    space=U[0]
    U[0]=U[6]
    U[6]=U[4]
    U[4]=U[2]
    U[2]=space
    space=U[7]
    U[7]=U[5]
    U[5]=U[3]
    U[3]=U[1]
    U[1]=space
    space=D[0]
    D[0]=D[2]
    D[2]=D[4]
    D[4]=D[6]
    D[6]=space
    space=D[1]
    D[1]=D[3]
    D[3]=D[5]
    D[5]=D[7]
    D[7]=space
def do_Yp():
    for i in range(3):
        do_Y()
def do_Z():
    space=[' ']*9
    for i in range(9):
        space[i]=L[i]
    L[0],L[1],L[2],L[3],L[4],L[5],L[6],L[7],L[8]=D[6],D[7],D[0],D[1],D[2],D[3],D[4],D[5],D[8]
    D[6],D[7],D[0],D[1],D[2],D[3],D[4],D[5],D[8]=R[4],R[5],R[6],R[7],R[0],R[1],R[2],R[3],R[8]
    R[4],R[5],R[6],R[7],R[0],R[1],R[2],R[3],R[8]=U[2],U[3],U[4],U[5],U[6],U[7],U[0],U[1],U[8]
    U[2],U[3],U[4],U[5],U[6],U[7],U[0],U[1],U[8]=space[0],space[1],space[2],space[3],space[4],space[5],space[6],space[7],space[8]
    space=F[0]
    F[0]=F[6]
    F[6]=F[4]
    F[4]=F[2]
    F[2]=space
    space=F[7]
    F[7]=F[5]
    F[5]=F[3]
    F[3]=F[1]
    F[1]=space
    space=B[0]
    B[0]=B[2]
    B[2]=B[4]
    B[4]=B[6]
    B[6]=space
    space=B[1]
    B[1]=B[3]
    B[3]=B[5]
    B[5]=B[7]
    B[7]=space
def do_Zp():
    for i in range(3):
        do_Z()
def do_R():
    space=F[2]
    F[2]=D[2]
    D[2]=B[6]
    B[6]=U[2]
    U[2]=space
    space=F[3]
    F[3]=D[3]
    D[3]=B[7]
    B[7]=U[3]
    U[3]=space
    space=F[4]
    F[4]=D[4]
    D[4]=B[0]
    B[0]=U[4]
    U[4]=space
    space=R[0]
    R[0]=R[6]
    R[6]=R[4]
    R[4]=R[2]
    R[2]=space
    space=R[7]
    R[7]=R[5]
    R[5]=R[3]
    R[3]=R[1]
    R[1]=space
def do_Rp():
    for i in range(3):
        do_R()
def do_U():
    do_Z();do_R();do_Z();do_Z();do_Z()
def do_Up():
    for i in range(3):
        do_U()
def do_D():
    do_Zp()
    do_R()
    do_Z()
def do_Dp():
    do_Zp()
    do_Rp()
    do_Z()
def do_L():
    do_Z(); do_Z()
    do_R()
    do_Z(); do_Z()
def do_Lp():
    for i in range(3):
        do_L()
def do_F():
    do_Yp()
    do_R()
    do_Y()
def do_Fp():
    for i in range(3):
        do_F()
def do_B():
    do_Y(); do_Y()
    do_F()
    do_Y(); do_Y()
def do_Bp():
    for i in range(3):
        do_B()

def transform(a):
    todolist=list(a.split())
    for thing in todolist:
        if thing=='Z': do_Z()
        if thing=='Z2': do_Z(); do_Z()
        if thing=='Zp': do_Zp()
        if thing=='Y': do_Y()
        if thing=='Y2': do_Y(); do_Y()
        if thing=='Yp': do_Yp()
        if thing=='R': do_R()
        if thing=='R2': do_R(); do_R()
        if thing=='Rp': do_Rp()
        if thing=='U': do_U()
        if thing=='U2': do_U(); do_U()
        if thing=='Up': do_Up()
        if thing=='D': do_D()
        if thing=='D2': do_D(); do_D()
        if thing=='Dp': do_Dp()
        if thing=='L': do_L()
        if thing=='L2': do_L(); do_L()
        if thing=='Lp': do_Lp()
        if thing=='F': do_F()
        if thing=='F2': do_F(); do_F()
        if thing=='Fp': do_Fp()
        if thing=='B': do_B()
        if thing=='B2': do_B(); do_B()
        if thing=='Bp': do_Bp()

def insert_basic_cross(basic_cross_edge):
    global basic_cross_alg
    if basic_cross_edge==23: pass
    if basic_cross_edge==32: transform('Fp D Rp Dp'); basic_cross_alg+='Fp D Rp Dp '
    if basic_cross_edge==36: transform('Dp L D'); basic_cross_alg+='Dp L D '
    if basic_cross_edge==63: transform('Fp'); basic_cross_alg+='Fp '
    if basic_cross_edge==31: transform('Up Rp F R'); basic_cross_alg+='Up Rp F R '
    if basic_cross_edge==13: transform('F2'); basic_cross_alg+='F2 '
    if basic_cross_edge==34: transform('D Rp Dp'); basic_cross_alg+='D Rp Dp '
    if basic_cross_edge==43: transform('F'); basic_cross_alg+='F '
    if basic_cross_edge==61: transform('L Fp Lp'); basic_cross_alg+='L Fp Lp '
    if basic_cross_edge==16: transform('Up F2'); basic_cross_alg+='Up F2 '
    if basic_cross_edge==14: transform('D R2 Dp'); basic_cross_alg+='D R2 Dp '
    if basic_cross_edge==41: transform('Rp F R'); basic_cross_alg+='Rp F R '
    if basic_cross_edge==42: transform('R F'); basic_cross_alg+='R F '
    if basic_cross_edge==24: transform('R D Rp Dp'); basic_cross_alg+='R D Rp Dp '
    if basic_cross_edge==26: transform('Lp Dp L D'); basic_cross_alg+='Lp Dp L D '
    if basic_cross_edge==62: transform('Lp Fp'); basic_cross_alg+='Lp Fp '
    if basic_cross_edge==56: transform('Dp Lp D'); basic_cross_alg+='Dp Lp D '
    if basic_cross_edge==65: transform('D2 B D2'); basic_cross_alg+='D2 B D2 '
    if basic_cross_edge==51: transform('U Rp F R'); basic_cross_alg+='U Rp F R '
    if basic_cross_edge==15: transform('U2 F2'); basic_cross_alg+='U2 F2 '
    if basic_cross_edge==54: transform('D R Dp'); basic_cross_alg+='D R Dp '
    if basic_cross_edge==45: transform('D2 Bp D2'); basic_cross_alg+='D2 Bp D2 '
    if basic_cross_edge==52: transform('B D R Dp'); basic_cross_alg+='B D R Dp '
    if basic_cross_edge==25: transform('B D2 Bp D2'); basic_cross_alg+='B D2 Bp D2 '
def find_basic_cross_edge():
    if (F[5]==F[8] and D[1]==D[8]): return(23)
    if (F[5]==D[8] and D[1]==F[8]): return(32)
    if (L[3]==D[8] and F[7]==F[8]): return(63)
    if (F[7]==D[8] and L[3]==F[8]): return(36)
    if (U[5]==D[8] and F[1]==F[8]): return(13)
    if (F[1]==D[8] and U[5]==F[8]): return(31)
    if (R[7]==D[8] and F[3]==F[8]): return(43)
    if (F[3]==D[8] and R[7]==F[8]): return(34)
    if (D[7]==D[8] and L[5]==F[8]): return(26)
    if (L[5]==D[8] and D[7]==F[8]): return(62)
    if (U[7]==D[8] and L[1]==F[8]): return(16)
    if (L[1]==D[8] and U[7]==F[8]): return(61)
    if (U[3]==D[8] and R[1]==F[8]): return(14)
    if (R[1]==D[8] and U[3]==F[8]): return(41)
    if (R[5]==D[8] and D[3]==F[8]): return(42)
    if (R[5]==F[8] and D[8]==D[3]): return(24)
    if (U[1]==D[8] and B[1]==F[8]): return(15)
    if (U[1]==F[8] and B[1]==D[8]): return(51)
    if (B[7]==D[8] and R[3]==F[8]): return(54)
    if (R[3]==D[8] and B[7]==F[8]): return(45)
    if (D[5]==D[8] and B[5]==F[8]): return(25)
    if (D[5]==F[8] and B[5]==D[8]): return(52)
    if (B[3]==D[8] and L[7]==F[8]): return(56)
    if (B[3]==F[8] and L[7]==D[8]): return(65)
def do_basic_cross():
    global basic_cross_alg
    for _ in range(4):
        basic_cross_edge=find_basic_cross_edge()
        insert_basic_cross(basic_cross_edge)
        do_Y(); basic_cross_alg+='Y '
    print('Algorithm to get a cross on layer 1: '+ basic_cross_alg)

def insert_l2_edge(l2_edge):
    global l2_alg
    if l2_edge==34: pass
    if l2_edge==43: transform('R Up Rp U Fp U2 F Up F Rp Fp R'); l2_alg+='R Up Rp U Fp U2 F Up F Rp Fp R '
    if l2_edge==31: transform('U R Up Rp Up Fp U F'); l2_alg+='U R Up Rp Up Fp U F '
    if l2_edge==13: transform('U2 Fp U F U R Up Rp'); l2_alg+='U2 Fp U F U R Up Rp '
    if l2_edge==36: transform('F Up Fp Up Lp U L U2 R Up Rp Up Fp U F'); l2_alg+='F Up Fp Up Lp U L U2 R Up Rp Up Fp U F '
    if l2_edge==63: transform('F Up Fp Up Lp U L Up Fp U F U R Up Rp'); l2_alg+='F Up Fp Up Lp U L Up Fp U F U R Up Rp '
    if l2_edge==14: transform('Up Fp U F U R Up Rp'); l2_alg+='Up Fp U F U R Up Rp '
    if l2_edge==41: transform('U2 R Up Rp Up Fp U F'); l2_alg+='U2 R Up Rp Up Fp U F '
    if l2_edge==16: transform('U Fp U F U R Up Rp'); l2_alg+='U Fp U F U R Up Rp '
    if l2_edge==61: transform('R Up Rp Up Fp U F'); l2_alg+='R Up Rp Up Fp U F '
    if l2_edge==54: transform('B Up Bp Up Rp U R2 Up Rp Up Fp U F'); l2_alg+='B Up Bp Up Rp U R2 Up Rp Up Fp U F '
    if l2_edge==45: transform('B Up Bp Up Rp U R U Fp U F U R Up Rp'); l2_alg+='B Up Bp Up Rp U R U Fp U F U R Up Rp '
    if l2_edge==15: transform('Fp U F U R Up Rp'); l2_alg+='Fp U F U R Up Rp '
    if l2_edge==51: transform('Up R Up Rp Up Fp U F'); l2_alg+='Up R Up Rp Up Fp U F '
    if l2_edge==65: transform('Bp U B U L Up Lp Up Fp U F U R Up Rp'); l2_alg+='Bp U B U L Up Lp Up Fp U F U R Up Rp '
    if l2_edge==56: transform('Bp U B U L Up Lp U2 R Up Rp Up Fp U F'); l2_alg+='Bp U B U L Up Lp U2 R Up Rp Up Fp U F '
def find_l2_edge():
    if F[3]==F[8] and R[7]==R[8]: return 34
    if F[3]==R[8] and R[7]==F[8]: return 43
    if F[1]==F[8] and U[5]==R[8]: return 31
    if F[1]==R[8] and U[5]==F[8]: return 13
    if F[7]==F[8] and L[3]==R[8]: return 36
    if L[3]==F[8] and F[7]==R[8]: return 63
    if R[1]==F[8] and U[3]==R[8]: return 41
    if R[1]==R[8] and U[3]==F[8]: return 14
    if L[1]==F[8] and U[7]==R[8]: return 61
    if U[7]==F[8] and L[1]==R[8]: return 16
    if R[3]==F[8] and B[7]==R[8]: return 45
    if B[7]==F[8] and R[3]==R[8]: return 54
    if B[1]==F[8] and U[1]==R[8]: return 51
    if U[1]==F[8] and B[1]==R[8]: return 15
    if L[7]==F[8] and B[3]==R[8]: return 65
    if B[3]==F[8] and L[7]==R[8]: return 56
def insert_l2_corner(l2_corner):
    global l2_alg
    if l2_corner==234: pass
    if l2_corner==342: transform('R Up Rp U R Up Rp'); l2_alg+='R Up Rp U R Up Rp '
    if l2_corner==423: transform('R U Rp Up F Rp Fp R'); l2_alg+='R U Rp Up F Rp Fp R '
    if l2_corner==431: transform('R U Rp'); l2_alg+='R U Rp '
    if l2_corner==314: transform('U R Up Rp'); l2_alg+='U R Up Rp '
    if l2_corner==143: transform('U R U2 Rp U R Up Rp'); l2_alg+='U R U2 Rp U R Up Rp '
    if l2_corner==541: transform('Fp U F'); l2_alg+='Fp U F '
    if l2_corner==415: transform('U2 R Up Rp'); l2_alg+='U2 R Up Rp '
    if l2_corner==154: transform('U2 R U2 Rp U R Up Rp'); l2_alg+='U2 R U2 Rp U R Up Rp '
    if l2_corner==524: transform('B U Bp R U Rp'); l2_alg+='B U Bp R U Rp '
    if l2_corner==245: transform('B U Bp U R Up Rp'); l2_alg+='B U Bp U R Up Rp '
    if l2_corner==452: transform('B U Bp U R U2 Rp U R Up Rp'); l2_alg+='B U Bp U R U2 Rp U R Up Rp '
    if l2_corner==263: transform('Lp Up L F Rp Fp R'); l2_alg+='Lp Up L F Rp Fp R '
    if l2_corner==632: transform('Lp Up L U R Up Rp'); l2_alg+='Lp Up L U R Up Rp '
    if l2_corner==326: transform('Lp Up L U R U2 Rp U R Up Rp'); l2_alg+='Lp Up L U R U2 Rp U R Up Rp '
    if l2_corner==136: transform('Up U R U2 Rp U R Up Rp'); l2_alg+='Up U R U2 Rp U R Up Rp '
    if l2_corner==361: transform('Up R U Rp'); l2_alg+='Up R U Rp '
    if l2_corner==613: transform('R Up Rp'); l2_alg+='R Up Rp '
    if l2_corner==651: transform('Fp U2 F'); l2_alg+='Fp U2 F '
    if l2_corner==516: transform('R U2 Rp'); l2_alg+='R U2 Rp '
    if l2_corner==165: transform('R U Rp U R Up Rp'); l2_alg+='R U Rp U R Up Rp '
    if l2_corner==562: transform('L Up Lp R U2 Rp'); l2_alg+='L Up Lp R U2 Rp '
    if l2_corner==625: transform('L U Lp Fp U F'); l2_alg+='L U Lp Fp U F '
    if l2_corner==256: transform('L Up Lp Fp U2 F'); l2_alg+='L Up Lp Fp U2 F '
def find_l2_corner():
    if D[2]==D[8] and F[4]==F[8] and R[6]==R[8]: return 234
    if F[4]==D[8] and F[8]==R[6] and D[2]==R[8]: return 342
    if R[6]==D[8] and D[2]==F[8] and F[4]==R[8]: return 423
    if R[0]==D[8] and F[2]==F[8] and U[4]==R[8]: return 431
    if F[2]==D[8] and U[4]==F[8] and R[0]==F[8]: return 314
    if U[4]==D[8] and R[0]==F[8] and F[2]==R[8]: return 143
    if B[0]==D[8] and R[2]==F[8] and U[2]==R[8]: return 541
    if R[2]==D[8] and U[2]==F[8] and B[0]==R[8]: return 415
    if U[2]==D[8] and B[0]==F[8] and R[2]==R[8]: return 154
    if B[6]==D[8] and D[4]==F[8] and R[4]==R[8]: return 524
    if D[4]==D[8] and R[4]==F[8] and B[6]==R[8]: return 245
    if R[4]==D[8] and B[6]==F[8] and D[4]==R[8]: return 452
    if D[0]==D[8] and L[4]==F[8] and F[6]==R[8]: return 263
    if L[4]==D[8] and F[6]==F[8] and D[0]==R[8]: return 632
    if F[6]==D[8] and D[0]==F[8] and L[4]==R[8]: return 326
    if U[6]==D[8] and F[0]==F[8] and L[2]==R[8]: return 136
    if F[0]==D[8] and L[2]==F[8] and U[6]==R[8]: return 361
    if L[2]==D[8] and U[6]==F[8] and F[0]==R[8]: return 613
    if L[0]==D[8] and B[2]==F[8] and U[0]==R[8]: return 651
    if B[2]==D[8] and U[0]==F[8] and L[0]==R[8]: return 516
    if U[0]==D[8] and L[0]==F[8] and B[2]==R[8]: return 165
    if B[4]==D[8] and L[6]==F[8] and D[6]==R[8]: return 562
    if L[6]==D[8] and D[6]==F[8] and B[4]==R[8]: return 625
def do_second_layer():
    global l2_alg
    for _ in range(4):
        l2_alg=''
        l2_corner=find_l2_corner()
        insert_l2_corner(l2_corner)
        l2_edge=find_l2_edge()
        insert_l2_edge(l2_edge)
        do_Y(); l2_alg+='Y '
        print('Algorithm to get block',_+1,'of layer 2: '+l2_alg)

def is_oll_cross():
    if U[8]==U[1]==U[3]==U[5]==U[7]:
        return 'cross'
    elif U[8]!=U[1] and U[8]!=U[3] and U[8]!=U[5] and U[8]!=U[7]:
        return 'dot'
    elif U[8]==U[1]==U[7] and U[3]!=U[8]!=U[5]:
        return 'l'
    elif U[1]!=U[8]!=U[5] and U[8]==U[3]==U[7]:
        return 'line'
    else:
        return 'meh'
def get_cross_done():
    global oll_cross_alg
    while True:
        if is_oll_cross()=='meh':
            do_U(); oll_cross_alg+='U '
            continue
        break
    if is_oll_cross()=='cross': pass
    elif is_oll_cross()=='dot': transform('F U R Up Rp Fp'); oll_cross_alg+='F U R Up Rp Fp '; get_cross_done()
    elif is_oll_cross()=='l': transform('F U R Up Rp Fp'); oll_cross_alg+='F U R Up Rp Fp '
    elif is_oll_cross()=='line': transform('F R U Rp Up Fp'); oll_cross_alg+='F R U Rp Up Fp '
def do_oll_cross():
    get_cross_done()
    print('Algorithm to get a cross on layer 3: '+oll_cross_alg)

def do_oll_alg():
    global finish_oll_alg
    if U[8]==U[1]==U[0]==U[7]==U[5]==U[3]==F[0] and U[8] not in U[2]+U[4]+U[6]:
        transform('Rp Up R Up Rp U2 R'); finish_oll_alg+='Rp Up R Up Rp U2 R '
    elif  U[8]==U[1]==U[6]==U[7]==U[5]==U[3]==F[2] and U[8] not in U[2]+U[4]+U[0]:
        transform('R U Rp U R U2 Rp'); finish_oll_alg+='R U Rp U R U2 Rp '
    elif U[8]==U[1]==U[7]==U[5]==U[3]==L[0]==L[2]==R[0]==R[2] and U[8] not in U[0]+U[2]+U[4]+U[6]:
        transform('R U Rp U R Up Rp U R U2 R'); finish_oll_alg+='R U Rp U R Up Rp U R U2 R '
    elif U[8]==U[1]==U[7]==U[5]==U[3]==L[0]==L[2]==F[2]==B[0] and U[8] not in U[0]+U[2]+U[4]+U[6]:
        transform('R U2 R2 Up R2 Up R2 U2 R'); finish_oll_alg+='R U2 R2 Up R2 Up R2 U2 R '
    elif U[8]==U[1]==U[7]==U[5]==U[3]==U[2]==U[6]==R[0]==B[2] and U[8] not in U[0]+U[4]:
        transform('R Bp Rp F R B Rp Fp'); finish_oll_alg+='R Bp Rp F R B Rp Fp '
    elif U[8]==U[0]==U[1]==U[2]==U[3]==U[7]==U[5]==L[2]==R[0] and U[8] not in U[6]+U[4]:
        transform('R B Rp F R Bp Rp Fp'); finish_oll_alg+='R B Rp F R Bp Rp Fp '
    elif U[8]==U[0]==U[1]==U[2]==U[3]==U[7]==U[5]==F[2]==F[0] and U[8] not in U[6]+U[4]:
        transform('R2 D Rp U2 R Dp Rp U2 Rp'); finish_oll_alg+='R2 D Rp U2 R Dp Rp U2 Rp '
    else: transform('U'); finish_oll_alg+='U '; do_oll_alg()
def do_oll():
    global finish_oll_alg
    do_oll_alg()
    print('Algorithm to finish  OLL on layer 3: '+finish_oll_alg)

def do_pll_alg():
    global pll_alg
    if F[0]==F[1]==F[2] and R[0]==R[1]==R[2] and B[0]==B[1]==B[2] and L[0]==L[1]==L[2]:
        pass
    elif F[1]==B[0]==B[2] and F[0]==F[2]==B[1] and L[0]==L[2]==R[1] and L[1]==R[0]==R[2]:
        transform('R2 U2 R U2 R2 U2 R2 U2 R U2 R2'); pll_alg+='R2 U2 R U2 R2 U2 R2 U2 R U2 R2 '
    elif B[0]==B[1]==B[2] and R[0]==R[2]==F[1] and R[1]==L[0]==L[2] and F[0]==F[2]==L[1]:
        transform('R Up R U R U R Up Rp Up R2'); pll_alg+='R Up R U R U R Up Rp Up R2 '
    elif B[0]==B[1]==B[2] and R[0]==R[2]==L[1] and F[1]==L[0]==L[2] and F[0]==F[2]==R[1]:
        transform('R2 U R U Rp Up Rp Up Rp U Rp'); pll_alg+='R2 U R U Rp Up Rp Up Rp U Rp '
    elif F[0]==F[2]==R[1] and L[0]==L[2]==B[1] and B[0]==B[2]==L[1] and R[0]==R[2]==F[1]:
        transform('Rp Up R2 U R U Rp Up R U R Up R Up Rp'); pll_alg+='Rp Up R2 U R U Rp Up R U R Up R Up Rp '
    elif F[0]==F[1]==R[2] and L[1]==L[2]==R[0] and B[0]==B[2]==R[1] and F[2]==L[0]==B[1]:
        transform('Rp F Rp B2 R Fp Rp B2 R2'); pll_alg+='Rp F Rp B2 R Fp Rp B2 R2 '
    elif F[0]==F[2]==R[1] and L[0]==L[1]==R[2] and B[1]==B[2]==R[0] and F[1]==L[2]==B[0]:
        transform('R Bp R F2 Rp B R F2 R2'); pll_alg+='R Bp R F2 Rp B R F2 R2 '
    elif F[1]==L[2]==R[0] and L[1]==F[2]==B[0] and B[1]==L[0]==R[2] and R[1]==F[0]==B[2]:
        transform('R2 U Rp Up Y R U Rp Up R U Rp Up R U Rp Yp R Up R2'); pll_alg+='R2 U Rp Up Y R U Rp Up R U Rp Up R U Rp Yp R Up R2 '
    elif F[0]==F[1]==F[2] and L[1]==B[2]==R[0] and B[1]==R[2]==L[0] and R[1]==B[0]==L[2]:
        transform('Rp U R Up R2 Fp Up F U R F Rp Fp R2 Up'); pll_alg+='Rp U R Up R2 Fp Up F U R F Rp Fp R2 Up '
    elif F[1]==L[2]==B[0] and L[1]==R[0]==B[2] and B[1]==F[0]==F[2] and R[1]==R[2]==L[0]:
        transform('R2 U Rp U Rp Up R Up R2 D Up Rp U R Dp'); pll_alg+='R2 U Rp U Rp Up R Up R2 D Up Rp U R Dp '
    elif F[1]==R[0]==B[2] and L[1]==B[0]==F[2] and B[1]==L[0]==L[2] and R[1]==R[2]==F[0]:
        transform('Rp Up R U Dp R2 U Rp U R Up R Up R2 D'); pll_alg+='Rp Up R U Dp R2 U Rp U R Up R Up R2 D '
    elif F[1]==R[0]==B[2] and L[0]==L[1]==R[2] and F[0]==F[2]==B[1] and L[2]==B[0]==R[1]:
        transform('Y R2 Dp F Up F U Fp D R2 B Up Bp'); pll_alg+='Y R2 Dp F Up F U Fp D R2 B Up Bp '
    elif F[1]==L[0]==L[2] and L[1]==B[0]==F[2] and B[1]==R[2]==F[0] and R[0]==R[1]==B[2]:
        transform('R U Rp F2 Dp L Up Lp U Lp D F2'); pll_alg+='R U Rp F2 Dp L Up Lp U Lp D F2 '
    elif F[0]==F[1]==B[2] and L[0]==L[1]==F[2] and B[0]==B[1]==L[2] and R[0]==R[1]==R[2]:
        transform('Bp U Fp U2 B Up Bp U2 F B Up');pll_alg+='Bp U Fp U2 B Up Bp U2 F B Up '
    elif F[1]==F[2]==B[0] and L[0]==L[1]==L[2] and B[1]==B[2]==R[0] and R[1]==R[2]==F[0]:
        transform('R U Rp Fp R U Rp Up Rp F R2 Up Rp Up'); pll_alg+='R U Rp Fp R U Rp Up Rp F R2 Up Rp Up '
    elif F[1]==F[2]==B[0] and L[1]==L[2]==R[0] and B[1]==B[2]==F[0] and R[1]==R[2]==L[0]:
        transform('R U Rp U R U Rp Fp R U Rp Up Rp F R2 Up R2 U2 R Up Rp'); pll_alg+='R U Rp U R U Rp Fp R U Rp Up Rp F R2 Up R2 U2 R Up Rp '
    elif F[0]==F[1]==B[2] and L[0]==L[1]==R[2] and B[0]==B[1]==F[2] and R[0]==R[1]==L[2]:
        transform('Rp U Lp U2 R U Up L Rp U Lp U2 R Up L'); pll_alg+='Rp U Lp U2 RUUp L Rp U Lp U2 R Up L '
    elif F[1]==L[2]==R[0] and L[0]==L[1]==F[2] and F[0]==R[2]==B[1] and R[1]==B[0]==B[2]:
        transform('R U2 Rp U2 R Bp Rp Up R U R B R2 U'); pll_alg+='R U2 Rp U2 R Bp Rp Up R U R B R2 U '
    elif F[1]==R[0]==B[2] and L[1]==L[2]==B[0] and L[0]==R[2]==B[1] and F[0]==F[2]==R[1]:
        transform('Rp U2 R U2 Rp F R U Rp Up Rp Fp R2'); pll_alg+='Rp U2 R U2 Rp F R U Rp Up Rp Fp R2 '
    elif F[0]==F[1]==R[2] and L[1]==F[2]==B[0] and B[1]==B[2]==R[0] and R[1]==L[0]==L[2]:
        transform('R U Rp Up Rp F R2 Up Rp Up R U Rp Fp');pll_alg+='R U Rp Up Rp F R2 Up Rp Up R U Rp Fp '
    elif F[0]==F[1]==B[2] and L[1]==L[2]==R[0] and B[1]==R[2]==L[0] and R[1]==F[2]==B[0]:
        transform('R U2 Rp D R Up R Up R U R2 D Rp Up R D2'); pll_alg+='R U2 Rp D R Up R Up R U R2 D Rp Up R D2 '
    elif F[0]==F[1]==B[2] and L[1]==B[0]==F[2] and B[1]==L[2]==R[0] and R[1]==R[2]==L[0]:
        transform('F R Up Rp Up R U Rp Fp R U Rp Up Rp F R Fp'); pll_alg+='F R Up Rp Up R U Rp Fp R U Rp Up Rp F R Fp '
    else: transform('U'); pll_alg+='U '; do_pll_alg()
def do_pll():
    global pll_alg
    do_pll_alg()
    if F[1]==F[8]: pass
    elif L[1]==F[8]: transform('Up'); pll_alg+='Up '
    elif B[1]==F[8]: transform('U2'); pll_alg+='U2 '
    elif R[1]==F[8]: transform('U'); pll_alg+='U '
    print('Algorithm to finish  PLL on layer 3: '+pll_alg)

def getinput():
    global F,R,B,L,U,D
    print('Example input: ygggywgyr ooowrorrg wwrboywgo wogrwyyrb grbwyoryy obbbbgbbw\n')
    f,r,b,l,u,d=input('Enter configuration: ').upper().split()
    F,R,B,L,U,D=list(f),list(r),list(b),list(l),list(u),list(d)
    print('Current configuration:')
    printconfig()
def printconfig():
    print('     '+U[0]+U[1]+U[2])
    print('     '+U[7]+U[8]+U[3])
    print('     '+U[6]+U[5]+U[4]+'\n')
    print(L[0]+L[1]+L[2]+'  '+F[0]+F[1]+F[2]+'  '+R[0]+R[1]+R[2]+'  '+B[0]+B[1]+B[2])
    print(L[7]+L[8]+L[3]+'  '+F[7]+F[8]+F[3]+'  '+R[7]+R[8]+R[3]+'  '+B[7]+B[8]+B[3])
    print(L[6]+L[5]+L[4]+'  '+F[6]+F[5]+F[4]+'  '+R[6]+R[5]+R[4]+'  '+B[6]+B[5]+B[4]+'\n')
    print('     '+D[0]+D[1]+D[2])
    print('     '+D[7]+D[8]+D[3])
    print('     '+D[6]+D[5]+D[4]+'\n')
    pass

print('''This program solves your jumbled 3x3 cube.
Enter the configuration as mentioned below:
-Keep red face in front with yellow face on top.
-Enter clockwise, the colours on each of the faces red, green, orange, blue, yellow and white
-Do this in an orderly fashion as space separated letters in separate lines''')
F,R,B,L,U,D=[],[],[],[],[],[]
basic_cross_alg,l2_alg,oll_cross_alg,finish_oll_alg,pll_alg='','','','',''
getinput()
do_basic_cross()
do_second_layer()
do_oll_cross()
do_oll()
do_pll()
print('\nThe cube must now be solved')
