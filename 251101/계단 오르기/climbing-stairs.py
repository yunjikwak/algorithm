N = int(input())
dp = [-1]*(1005)

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, N+1):
    dp[i] = dp[i-2] + dp[i-3]

if dp[N] != -1:
    print(dp[N]%10007)
else:
    print(0)