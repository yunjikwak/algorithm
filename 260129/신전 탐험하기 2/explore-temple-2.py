N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]

for i in range(3):
    dp[1][i][i] = arr[0][i]
    
for i in range(2, N+1):
    for j in range(3):
        for k in range(3):
            if j == k:
                continue
            for s in range(3):
                if dp[i-1][k][s] == 0:
                    continue
                dp[i][j][s] = max(dp[i][j][s], dp[i-1][k][s]+arr[i-1][j])

result = 0
for i in range(3):
    for j in range(3):
        if i == j:
            continue
        result = max(result, dp[N][i][j])

print(result)