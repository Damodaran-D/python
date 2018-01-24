#!/bin/python3

import sys

def getWays(n, c):
    # Complete this function
    dp=[0]*(n+1)
    dp[0]=1
    sorted(c)
    for i in c:
        for j in range(i,n+1):
            dp[j]+=dp[j-i]
        print(dp)
    return dp[n]
n, m = input().strip().split(' ')
n, m = [int(n), int(m)]
c = list(map(int, input().strip().split(' ')))
# Print the number of ways of making change for 'n' units using coins having the values given by 'c'
ways = getWays(n, c)
print(ways)
