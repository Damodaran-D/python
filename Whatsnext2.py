T = int(input())
for i in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    if n==1:
        num=[ 1, 1, num[0]-1]
    elif n==2:
        num=[ 1, num[1]+1, num[0]-1]
    elif n%2==1:
        if num[n-1]==1:
            num=num[:n-3]+[num[n-3]+1, 1, num[n-1]-1]
        else:
            num=num[:n-2]+[num[n-2]-1, 1, 1, num[n-1]-1]
    else:
        if num[n-3]==1:
            num=num[:n-4]+[num[n-4]+1, num[n-1]+1, num[n-2]-1]
        else:
            num=num[:n-3]+[num[n-3]-1, 1, num[n-1]+1, num[n-2]-1]
        
    while num[-1] == 0:
        num = num[:-1]
    while 0 in num:
        m = num.index(0)
        num = num[:m-1] + [num[m-1]+num[m+1]] + num[m+2:]
    print (len(num))
    print (' '.join(map(str, num)))
