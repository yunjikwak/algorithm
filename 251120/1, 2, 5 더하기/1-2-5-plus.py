N = int(input())

dp = [0] * (N+1)
dp[0] = 1

for i in range(1, N+1):
    if i >= 1:
        dp[i] += dp[i-1]
    
    if i >= 2:
        dp[i] += dp[i-2]
        
    if i >= 5:
        dp[i] += dp[i-5]

    dp[i] %= 10007

print(dp[N])