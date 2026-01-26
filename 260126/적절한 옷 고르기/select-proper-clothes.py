N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[-1] * N for _ in range(M + 1)]

for j in range(N):
    s, e, v = arr[j]
    if s <= 1 <= e:
        dp[1][j] = 0

for i in range(2, M + 1):
    for j in range(N):
        if not (arr[j][0] <= i <= arr[j][1]):
            continue

        for k in range(N):
            if dp[i-1][k] != -1:
                val = abs(arr[j][2] - arr[k][2])
                dp[i][j] = max(dp[i][j], dp[i-1][k] + val)

print(max(dp[M]))