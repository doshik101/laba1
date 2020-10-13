import math
def Exp(x):
    n=1
    exp=1
    m=1
    while(m>0.0001):
        m=(x**n)/(math.factorial(n))
        n=n+1
        exp=exp+round(m,4)
    return(exp)
x=int(input("Ведите степень е: "))
print(Exp(x))





def Sin(x):
    n=2;
    m=1;
    sin=x;
    while(round(abs(m),4)>0.001):
        m=(-1**(n-1))*(x**(2*n-1))/(math.factorial(2*n-1))
        sin=round(sin,4)+round(m,4)
        n=n+1
    return(sin)
x=float(input("Ведите x: "))
print(Sin(x))





def Cos(x):
    n=2;
    m=1;
    cos=x;
    while(round(abs(m),4)>0.001):
        m=(-1**(n-1))*(x**(2*n-2))/(math.factorial(2*n-2))
        cos=round(cos,4)+round(m,4)
        n=n+1
    return(cos)
x=float(input("Ведите x: "))
print(Cos(x))



