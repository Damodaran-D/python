T = int(input())
for i in range(T):
    n = int(input())
    num = list(map(int, input().split()))
    if n==1:
        if num[0]>1:
            num=[ 1, 1, num[0]-1]
        else:
             num=[1, 1]
        
    elif n==2:
        if num[0]==1:
            num=[ 1, num[1]+1]
        else:
            num=[1, num[1]+1, num[0]-1]
    elif n%2==0:
        app=num[:-4]
        a,b,c,d = num[-4:]
        if b > 1:
            if c > 1:
                num=app+[a, b-1, 1, d+1, c-1]
            else:
                num=app+[a, b-1, 1, d+1]
        elif c > 1:
            num=app+[a+1, d+1, c-1]
        else:
            num=app+[a+1, d+1]

    else:
        app=num[:-3]
        a, b, c = num[-3:]
        if b > 1:
            if c > 1:
                num=app+[a, b-1, 1, 1, c-1]
            else:
                num=app+[a, b-1, 1, 1]
        elif c > 1:
            num=app+[a+1, 1, c-1]
        else:
            num=app+[a+1, 1]
    
##    while num[-1] == 0:
##        num = num[:-1]
##    while 0 in num:
##        m = num.index(0)
##        num = num[:m-1] + [num[m-1]+num[m+1]] + num[m+2:]
    print (len(num))
    print (' '.join(map(str, num)))
