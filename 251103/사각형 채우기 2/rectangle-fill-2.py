N = int(input())

dp = [-1] * 1002
dp[1] = 1
dp [2] = 3

for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]*2

print(dp[N]%10007)