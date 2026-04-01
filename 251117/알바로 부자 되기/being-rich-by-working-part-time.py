N = int(input())
arr = []
for _ in range(N):
    # s, e, p = map(int, input().split())
    # arr.append((s, e, p))
    arr.append(list(map(int, input().split())))

dp = [0] * (N+1)

for i in range(N):
    start, end, coin = arr[i]
    dp[i] = coin
    for j in range(i):
        if arr[j][1] < start:
            dp[i] = max(dp[j]+coin, dp[i])

print(max(dp))