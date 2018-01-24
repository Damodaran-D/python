def solve():
    l = int(input())
    s = list(input())

    flag = 1
    while flag:
        flag = 0
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                flag = 1
                s = list(filter((s[i]).__ne__, s))
                break
    
    count = 0
    s1 = list(set(s))
    print(s1)

    if len(s1) < 2:
        return 0
    elif len(s1) == 2:
        return len(s)       

    for i in range(len(s1)-1):
        for j in range(i, len(s1)):
            t = ""
            for x in s:
                if x == s1[i] or x == s1[j]:
                    t += x
            if t.count(s1[i]+s1[i]) == 0 and t.count(s1[j]+s1[j]) == 0:
                count = max(count, len(t))

    return count
             
print(solve())
