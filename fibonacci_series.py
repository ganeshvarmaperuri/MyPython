def fibnacci(n):
    a,b = 0,1
    for i in range(n):
        c = a+b
        print(c)
        a=b
        b=c
    return

n=int(input('Enter n value to Print Fibonacci Series:'))


fibnacci(n)
