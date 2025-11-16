N = int(input())
arr = list(map(int, input().split()))

dp = [[1, 1] for _ in range(N)] # 증 - 감

for i in range(N):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i][0] = max(dp[i][0], dp[j][0] + 1)
        elif arr[j] > arr[i]:
            dp[i][1] = max(dp[i][1], dp[j][0] + 1) # 증 -> 감
            dp[i][1] = max(dp[i][1], dp[j][1] + 1) # 감 -> 감

result = 0
for i in range(N):
    result = max(result, dp[i][0], dp[i][1])

print(result)