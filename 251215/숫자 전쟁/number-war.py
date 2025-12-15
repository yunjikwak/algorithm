N = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(N-1, -1, -1):
    for j in range(N-1, -1, -1):
        if first[i] > second[j]:
            dp[i][j] = max(second[j] + dp[i][j + 1], dp[i + 1][j + 1])
        elif first[i] < second[j]:
            dp[i][j] = max(dp[i + 1][j], dp[i + 1][j + 1])
        else:
            dp[i][j] = dp[i + 1][j + 1]

print(dp[0][0])