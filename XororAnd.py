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

n=int(input())
A = list(map(int,input().split()))

s=Stack()
r=-1
rr=[]
for i in A:
    r=-1
    while not s.isEmpty():
        r=max(r,(i & s.peek()) ^ (i | s.peek())) & (i ^ s.peek())
        print(r)
        if i<s.peek():
            s.pop()
        else:
            break
    s.push(i)
    rr.append(r)
print(max(rr))
