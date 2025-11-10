N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * N for _ in range(N)]

dp[0][0] = arr[0][0]

for j in range(1, N):
    dp[0][j] = max(dp[0][j-1], arr[0][j])

for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], arr[i][0])

for i in range(1, N):
    for j in range(1, N):
        dp[i][j] = min(max(dp[i-1][j], arr[i][j]), max(dp[i][j-1], arr[i][j]))

print(dp[N-1][N-1])
