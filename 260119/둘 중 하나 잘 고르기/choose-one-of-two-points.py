N = int(input())

cards = [tuple(map(int, input().split())) for _ in range(2*N)]

dp = [[-float('inf')] * (N + 1) for _ in range(2*N + 1)]
dp[0][0] = 0

for i in range(1, 2*N+1):
    red, blue = cards[i-1]

    for j in range(N+1):
        if j > 0:
            if dp[i-1][j-1] != -float('inf'):
                dp[i][j] = max(dp[i-1][j-1]+red, dp[i][j])

        if (i - j) <= N:
            if dp[i-1][j] != -float('inf'):
                dp[i][j] = max(dp[i][j], dp[i-1][j]+blue)

print(dp[2 * N][N])