
n=input()
from heapq import heappush, heappop

max_heap = []
min_heap = []

for i in range(int(n)):
    num=int(input())
    
    if not max_heap or num > -max_heap[0]:
        heappush(min_heap, num)
        if len(min_heap) > len(max_heap) + 1:
            heappush(max_heap, -heappop(min_heap))
    else:
        heappush(max_heap, -num)
        if len(max_heap) > len(min_heap):
            heappush(min_heap, -heappop(max_heap))

    if len(min_heap) == len(max_heap):
            print((-max_heap[0] + min_heap[0]) / 2.0 )
    else:
        print(min_heap[0]/1.0)

