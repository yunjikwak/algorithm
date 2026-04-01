N = int(input())

dp = [-1] * 1005

dp[0] = 1
dp[1] = 2
dp[2] = 7
for i in range(3, N+1):
    dp[i] = dp[i-1]*3 + dp[i-2] - dp[i-3]

print(dp[N]%1000000007)