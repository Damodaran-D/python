class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)

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
n,q=5,1
number=[3 ,4 ,7 , 6, 5]
#n,q=10,2
#number=[1,8,11,23,18,2,15,30,4,5]
s=Stack()
a=Stack()
b=Stack()

for i in number:
    s.push(i)

for i in range(q):
    while not s.isEmpty():
        j=s.pop()
        #print("Hi")
        if j%nprime(i+1)==0:
            a.push(j)
        else:
            b.push(j)
    
    while not a.isEmpty():
        print(a.pop())
    
    s=b
    b=Stack()
while not s.isEmpty():
        print(s.pop())
