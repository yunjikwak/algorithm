N, K = map(int, input().split())
arr = list(map(int, input().split()))

INF = -float('inf')
dp = [INF] * (K + 1)
result = INF

for num in arr:
    next_dp = [INF] * (K + 1)

    if num > 0:
        for k in range(K + 1):
            if dp[k] != INF:
                next_dp[k] = dp[k] + num
        next_dp[0] = max(next_dp[0], num)
    else:
        for k in range(1, K + 1):
            if dp[k-1] != INF:
                next_dp[k] = dp[k-1] + num
        
        next_dp[1] = max(next_dp[1], num)
    dp = next_dp
    
    cur = max(dp)
    if cur > result:
        result = cur

print(result)