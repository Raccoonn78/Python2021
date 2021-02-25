import math
import traceback


def function(x,y,z):
    one=float(71*(y**8))
    two=float(98*(z**2))
    three=float(34)
    four_parentheses=math.cos(x)-50*x
    four=math.tan(four_parentheses)
    five=math.tan(x)
    six=float(-41)
    seven=float(((y**7)+81*(x**6)-35)**5)
    eight=float(z**7)
    ull= one+two+three+four+five+six+seven+eight
    ul='%.2e' % ull
    
    return ul





def function2(x):
    if x<(-71):
        answer=71*(x**3)+98*(x**4)+34
    if x>=(-71) and x<=(-59):
        answer=(math.e)**(x**3)+x
    if x>=(-59) and x<=(-48):
        answer= (math.e)**( 33*(x**6)+math.log(x,math.e)+27)-63*x
    if (x<=20) and (x>=(-48)):
        one= (math.e)**(x**7)
        two=x**3
        three=57
        answer=one-two-three
        
    if x>=20:
        ones=(39*(x**7)-x**4)**2
        twos=49*(x**7)
        answer=ones+twos
    answer='%.2e'% answer

    return answer





def function3(n,m):
    n=n+1
    m=m+1
    one=0
    summ_one=0
    i=1
    j=1
    summ=0
    for i in range(n):
       summ_one=summ_one+summ
       summ=0
       for j in range(m):
           one=71*(j**8)+98*(j**2)+34
           summ=summ+one
    
    i=1
    j=1   
    two=0
    summ_two=0
    summ2=0
    for i in range(n):
       
       summ_two=summ_two+summ2
       summ2=0
       for j in range(m):
           two=math.tan(i)+(i**3)-5
           summ2=summ2+two
    
    answer=(3*summ_one)-(93*summ_two)
    answer2='%.2e' % answer
    return answer2




    
def ten(f):
    f=f/10

    return f
def recursion(n):
    if n <2:
        f=2
    else:
        f=math.fabs(recursion(n-1))+math.fabs(recursion(n-1))+60   
    return f

def function4(n):
    f=recursion(n);
    f='%.2e' % f
    return f


try:    
    assert function(63,-19,-9)==  "3.33e+63"
    assert function(13,-75,9)== "-4.24e+65"

    assert function2(1)== "-5.53e+01"
    assert function2(59)== "9.42e+27"


    assert function3(25,62)==  "8.60e+18"
    assert function3(83,48)==  "2.91e+18"

    assert function4(2)==  "6.40e+01"
    assert function4(4)==  "4.36e+02"
except AssertionError:
    print("TEST ERROR")
    traceback.print_exc()
else:
    print("TEST PASSED")
