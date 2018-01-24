n=input()
##a=[]
##for i in range(int(n)):
##    a.append(int(input()))
##    a.sort()
##    if len(a)%2==0:
##        print((a[int(i/2)]+a[int(i/2)+1])/2)
##    else:
##        print(float(a[int(i/2)]))
##             


from heapq import heappush, heappop

class Median:
    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num):
        if not self.max_heap or num > -self.max_heap[0]:
            heappush(self.min_heap, num)
            if len(self.min_heap) > len(self.max_heap) + 1:
                heappush(self.max_heap, -heappop(self.min_heap))
        else:
            heappush(self.max_heap, -num)
            if len(self.max_heap) > len(self.min_heap):
                heappush(self.min_heap, -heappop(self.max_heap))

    def findMedian(self):
        if len(self.min_heap) == len(self.max_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2.0 
        return  self.min_heap[0]

mf = Median()
for i in range(int(n)):
    mf.addNum(int(input()))
    a=int(input())
    
    print(mf.findMedian()/1.0)
