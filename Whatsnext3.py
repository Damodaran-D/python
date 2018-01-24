# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    a = list(map(int, input().strip().split()))
    c = [1] + a
    if n % 2 == 1:
        c[n-1] -= 1
        c[n] -= 1
        c = c[1:n] + [1, 1]  + [c[n]]
    else:
        c[n-2] -= 1
        c[n-1] -= 1
        c = c[1:n-1] + [1, c[n]+1] + [c[n-1]]
    while c[-1] == 0:
        c = c[:-1]
    while 0 in c:
        m = c.index(0)
        c = c[:m-1] + [c[m-1]+c[m+1]] + c[m+2:]
    print (len(c))
    print (" ".join(str(ci) for ci in c))
    
