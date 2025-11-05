N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[0] * (N+1) for _ in range(N+1) ]

def init():
    dp[0][0] = arr[0][0]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][0], arr[i][0])

    for i in range(1, N):
        dp[0][i] = min(dp[0][i-1], arr[0][i])

init()

for i in range(1, N):
    for j in range(1, N):

        dp[i][j] = min(max(dp[i-1][j], dp[i][j-1]), arr[i][j])

print(dp[N-1][N-1])