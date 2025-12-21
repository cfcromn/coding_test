import sys
input = sys.stdin.readline

n = int(input())
dp = [0, 1, 1, 1, 2, 2] + [0] * 95
top = 5

for _ in range(n):
    m = int(input())
    if m <= top:
        print(dp[m])
    else:
        for i in range(top, m + 1):
            dp[i] = dp[i - 1] + dp[i - 5]
        top = m
        print(dp[top])