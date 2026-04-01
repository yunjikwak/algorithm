N, K = map(int, input().split())
arr = input().strip()

dp = [[0] * (K+1) for _ in range(N + 1)]

for i in range(1, N + 1):
    cur = arr[i-1]
    for j in range(K + 1):
        a = 0
        if j%2 == 0 and cur == 'L':
            a = 1
        elif j%2 == 1 and cur == 'R':
            a = 1

        if j == 0:
            dp[i][j] = dp[i-1][j] + a
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-1]) + a

print(max(dp[N]))