N = int(input())

arr = []
for _ in range(N):
    x, y = map(int, input().split())
    arr.append((x, y))

dp = [1] * (N+1)

arr.sort(key=lambda x:x[0])

for i in range(N):
    start, end = arr[i]
    for j in range(i):
        if arr[j][1] < start:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))