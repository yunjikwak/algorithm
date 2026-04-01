N, M = map(int, input().split())
arr = list(map(int, input().split()))

dp = [[0] * 41 for _ in range(N)]
dp[0][arr[0] + 20] += 1
dp[0][-arr[0] + 20] += 1

for i in range(N - 1):
    for j in range(41):
        if dp[i][j] == 0:
            continue

        cur = j-20
        next = arr[i+1]

        if cur+next <= 20:
            dp[i+1][cur+next+20] += dp[i][j]
        if cur-next >= -20:
            dp[i+1][cur-next+20] += dp[i][j]

print(dp[N-1][M + 20])