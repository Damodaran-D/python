import heapq
#n, k = input().strip().split(' ')
#n, k = [int(n), int(k)]
n=6
k=7
A=[1 ,2 ,3 ,9 ,10 ,12]
A=[10]

i=0
#A = list(map(int,input().split()))
heapq.heapify(A)
print(sum(A))
if sum(A) >= k and A[0]<k:
 
    
    while A[0] < k:
        a=heapq.heappop(A)
        b=heapq.heappop(A)
        heapq.heappush(A, a+2*b)
        i+=1
        if i>n:
            break
    
    if i<=n:
        print(i)
    else:
        print(-1)
else:
    print(-1)
