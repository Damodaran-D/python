def solve(n, a):
    if n == 1:
        ans = [1, 1, a[0] - 1]
    elif n == 2:
        ans = [1, a[1] + 1, a[0] - 1]
    elif n % 2 == 1:
        if a[n - 2] == 1:
            ans = a[0:n - 3] + [a[n - 3] + 1, 1, a[n - 1] - 1]
        else:
            ans = a[0:n - 2] + [a[n - 2] - 1, 1, 1, a[n - 1] - 1]
    else:
        if a[n - 3] == 1:
            ans = a[0:n - 4] + [a[n - 4] + 1, a[n - 1] + 1, a[n - 2] - 1]
        else:
            ans = a[0:n - 3] + [a[n - 3] - 1, 1, a[n - 1] + 1, a[n - 2] - 1]

    if ans[-1] == 0:
        ans = ans[:-1]

    return ans

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        a = list(map(int, input().split()))

        ans = solve(n, a)
        print (len(ans))
        print (' '.join(map(str, ans)))

