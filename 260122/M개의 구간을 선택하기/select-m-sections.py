N, M = map(int, input().split())
arr = list(map(int, input().split()))

# N번째 인덱스까지 M개의 구간 선택했고 현재 인덱스 선택 여부(0, 1)
dp = [[[-float('inf')] * 2 for _ in range(M+1)] for _ in range(N+1)]

for i in range(N):
    dp[i][0][0] = 0

for i in range(1, N+1):
    cur = arr[i-1]
    for j in range(1, M+1):
        # 선택 안 함
        dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1])

        # 선택 함
        dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0]) + cur

print(max(dp[N][M][0], dp[N][M][1]))