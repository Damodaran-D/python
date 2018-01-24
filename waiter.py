import math
import sys

def nprime(nth):
   s = 1
   n = 0
   while n < nth:
       s += 1
       for x in range(2,s):
          if s % x == 0:
             break
       else:
          n += 1

   return s


##n, q = input().strip().split(' ')
##n, q = [int(n), int(q)]
##number = map(int, input().strip().split(' '))
##number=list(number)
##print(str(number)+" --- ")
n,q=5,1
number=[3 ,4 ,7 , 6, 5]
##n,q=5,2
##number=[3 , 3, 4, 4, 9]
a=[]
b=[]
for i in range(q):
    for j in number[::-1]:
        if j%nprime(i+1)==0:
            b.append(j)
        else:            
            a.append(j)
    print(b)
    print(a)
    for j in b[::-1]:
        print(j)
    b=[]
    number=a
    a=[]
for j in number[::-1]:
        print(j)
