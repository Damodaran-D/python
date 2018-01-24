def main():
    s_len = int(input().strip())
    s = input().strip()
    rep=[]
    m=s_len+1
    count=0
    for i in range(1,s_len):
        if s[i-1]==s[i]:
            rep.append(s[i])

    for i in rep:
        new=list(filter(lambda a: a != i, s))
    new1=list(set(new))

    if len(new1) < 2:
        return 0
    elif len(new1) == 2:
        return len(new)

    for i in new:
        fin=""
        for j in new1:
            for k in new1:
                if i==j or i==k:
                    fin+=k
            if fin.count(i+i)==0 and fin.count(j+j)==0:
                count=max( count, len(fin))

    return count

print(main())
