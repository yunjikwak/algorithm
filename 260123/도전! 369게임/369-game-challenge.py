N = int(input())

dp = [0] * (N+1)

for i in range(1, N + 1):
    if i % 3 == 0 or '3' in str(i) or '6' in str(i) or '9' in str(i):
        dp[i] = dp[i-1] + 1
    else:
        dp[i] = dp[i-1]

print(dp[N])