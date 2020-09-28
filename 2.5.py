def F(a1=0, b1=0, c1=0, a2=0, b2=0, c2=0):
    D=a1*b2-a2*b1
    print('x=',(c1*b2-c2*b1)/D)
    print('y=',(a1*c2-a2*c1)/D)
a1,b1,c1,a2,b2,c2=map(int, input().split())
F(a1,b1,c1,a2,b2,c2)
