N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[-1] * 10 for _ in range(12)] for _ in range(N + 1)]
dp[0][0][0] = 0

for i in range(1, N+1):
    s, b = arr[i-1]

    for j in range(12):
        for k in range(10):
            if dp[i-1][j][k] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k])
            
            if j > 0 and dp[i-1][j-1][k] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j-1][k]+s)

            if k > 0 and dp[i-1][j][k-1] != -1:
                dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1]+b)

print(dp[N][11][9])