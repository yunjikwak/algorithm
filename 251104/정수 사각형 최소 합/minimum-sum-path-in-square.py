N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[-1] * 101 for _ in range(101)]

def init():
    dp[0][N-1] = arr[0][N-1]
    for i in range(N-2, -1, -1):
        dp[0][i] = dp[0][i+1] + arr[0][i]
    
    for i in range(1, N):
        dp[i][N-1] = dp[i-1][N-1] + arr[i][N-1]

init()

for i in range(1, N):
    for j in range(N-2, -1, -1):
        dp[i][j] = min(dp[i-1][j]+arr[i][j], dp[i][j+1]+arr[i][j])

print(dp[N-1][0])