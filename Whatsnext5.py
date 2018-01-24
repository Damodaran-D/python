def solve(B):
    if len(B) == 1:
        if B[0] > 1:
            return [1, 1, B[0] - 1]
        return [1, 1]
    elif len(B) == 2:
        a, b = B
        if a == 1:
            return [1, b + 1]
        return [1, b + 1, a - 1]
    elif len(B) % 2 == 0:
        pre = B[:-4]
        a, b, c, d = B[-4:]
        if b > 1:
            if c > 1:
                return pre + [a, b - 1, 1, d + 1, c - 1]
            return pre + [a, b - 1, 1, d + 1]
        if c > 1:
            return pre + [a + 1, d + 1, c - 1]
        return pre + [a + 1, d + 1]
    else:
        pre = B[:-3]
        a, b, c = B[-3:]
        if b > 1:
            if c > 1:
                return pre + [a, b - 1, 1, 1, c - 1]
            return pre + [a, b - 1, 1, 1]
        if c > 1:
            return pre + [a + 1, 1, c - 1]
        return pre + [a + 1, 1]

def main():
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))
        b = solve(a)
        print (len(b))
        print (" ".join(map(str, b)))

main()
