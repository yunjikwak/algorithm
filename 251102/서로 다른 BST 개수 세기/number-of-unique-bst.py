N = int(input())

dp = [-1] * 20
dp[1] = 1
dp[2] = 2

for i in range(3, N+1):
    dp[i] = dp[i-1]*2 + 1

print(dp[N])