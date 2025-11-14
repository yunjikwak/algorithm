N, M = map(int,input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

dp = [[1] * M for _ in range(N)]

dp[0][0] = 1

def init():
    for i in range(M):
        dp[0][i] = 0
    for i in range(N):
        dp[i][0] = 0

for i in range(N):
    for j in range(M):
        cur = arr[i][j]
        for k in range(i):
            for t in range(j):
                if arr[k][t] < cur:
                    dp[i][j] = max(dp[k][t]+1, dp[i][j])

answer = 0
for i in range(N):
    answer = max(answer, max(dp[i]))
print(answer)