N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [[-1] * 4 for _ in range(N + 1)]
dp[0][0] = 0

for i in range(N):
    for j in range(4):
        if dp[i][j] == -1:
            continue
            
        if i + 1 <= N and j + 1 <= 3:
            dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + arr[i+1])
            
        if i + 2 <= N:
            dp[i+2][j] = max(dp[i+2][j], dp[i][j] + arr[i+2])

print(max(dp[N]))