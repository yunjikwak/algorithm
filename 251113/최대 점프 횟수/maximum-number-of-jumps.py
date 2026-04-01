N = int(input())
arr = list(map(int, input().split()))

dp = [-1] * N

dp[0] = 0

for i in range(N):
    if dp[i] == -1:
        continue
    
    max_v = arr[i]
    
    for j in range(1, max_v + 1):
        if i + j < N:
            dp[i + j] = max(dp[i + j], dp[i] + 1)

print(max(dp))