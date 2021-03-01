import math
import traceback

def function(x):
    if x[1]=='eq':
        if x[0]== 1958:
            return 3
        elif x[0]==1959:
            if x[4]==2004:
                return 0
            elif x[4]==1990:
                if x[2]==1971:
                    return 2
                elif x[2]==1964:
                    return 1
    if x[1]=='ocaml':
        if x[2]==1971:
            if x[3]==1974:
                return 9
            elif x[3]==2005:
                return 10        
            else:
                return 11
        elif x[2]==1964:
            if x[3]== 1974:
                return 4
            elif x[3]==2005:
                if x[0]==1959:
                    return 5
                elif x[0]==1958:
                    return 6
            if x[3]==1982:
                if x[0]==1959:
                    return 7
                else:
                    return 8

def function2(x):
  
   a= x& 0x3
   a<<=21
   b=x&0xC
   b<<=17
   c=x&0x10
   c<<=14
   d=x&0x20
   d<<=18
   e=x&0x1FFFC0
   e>>=6
   f=x&0x1FE00000
   f<<=3
   g=x& 0x60000000
   g>>=14
   h=x&0x80000000
   h>>=14

   print(f | d | a | b | c | h | g |e)
   return f | d | a | b | c | h | g |e



    
def function3(x):
    for i in range(4):
        if x[i][1]==None:
            del x[i]
    
    free=[1,2,3,4]
    for i in range(4):
       free[i]=x[i][1]
    
    for i in range(4):
        free[i]=free[i].split('@')
        
    for i in range(4):
        x[i][1]=free[i][1]
    
    for i in range(4):
        if x[i][0]=='false':
            x[i][0]=0
        else:
            x[i][0]=1

    for i in range(4):
        x[i][2]=x[i][2]*100
        x[i][2]=math.ceil(x[i][2])
        x[i][2]=str(x[i][2])
        x[i][2]=x[i][2]+'%'
    
    rows_cnt = len(x)
    cols_cnt = len(x[0])
 
    new_matix = [[0]*rows_cnt for _ in range(cols_cnt)]

    for i in range(rows_cnt):
        for j in range(cols_cnt):
            new_matix[j][i] = x[i][j]
    for i in range(3):
        print(new_matix[i])
    return new_matix





try:    
   
    assert function([1958,'eq',1971,2005,1990]) == 3
    assert function([1959,'ocaml',1971,2005,1990]) == 10

    assert function2(0x693eed4b) == 0x4971fbb5
    assert function2(0x9346cc02) == 0x9a421b30

    assert function3([
                        ["false",'evgenij56@rambler.ru',0.159],
                        ['true','gukberg13@yandex.ru',0.127],
                        [None,None,None],
                        ['true','vladimir73@yandex.ru',0.886],
                        ['false','midskij81@yahoo.com', 0.176]
                        ]) == [ [0,1,1,0],
                            ['rambler.ru', 'yandex.ru','yandex.ru','yahoo.com'],
                            ['16%','13%','89%','18%']
                        ]
    assert function3([
                        ["true",'miroslav21@yahoo.com',0.092],
                        ['false','vaceslav38@mail.ru',0.410],
                        ['true','tuzuzman90@rambler.ru',0.797],
                        [None,None,None],
                        ['false','rinat44@yahooo.com', 0.329]
                        ]) == [
                            [1,0,1,0],
                            ['yahoo.com','mail.ru','rambler.ru','yahooo.com'],
                            ['10%','41%','80%','33%']
                        ]
  
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
