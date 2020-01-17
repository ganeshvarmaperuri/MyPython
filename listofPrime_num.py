
import random

def Prime(n,m):
    for num in range(n,m+1):
        if num>1:
            for i in range(2,num):
                if num%i == 0:
                    break
            else:
                print(num)

n= random.randint(10,25)
m= random.randint(n,50)
print('prime numbers between', n, 'and', m, 'is' )

Prime(n,m)


'''
def listofPrime(n,m):
    for num in range(n,m+1):
        if num>1:
            for i in range(2,num):
                if num % i == 0:
                    break
            else:
                print(num)

listofPrime(10,20)
'''