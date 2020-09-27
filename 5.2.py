def Max(a=0, b=0):
    if(a>b):
        return a
    elif(b>a):
        return b
    else:
        return "a=b"
a,b=map(int, input("определение максимального числа\nВведите два числа: ").split())
print(Max(a, b))
