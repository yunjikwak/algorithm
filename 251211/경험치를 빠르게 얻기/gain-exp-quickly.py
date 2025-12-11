N, M = map(int, input().split())
arr = []
for _ in range(N):
    e, t = map(int, input().split())
    arr.append((e, t))

MAX_TIME = 10000
dp = [0] * (MAX_TIME + 1)

for e, t in arr:
    for j in range(MAX_TIME, t-1, -1):
        dp[j] = max(dp[j], dp[j-t] + e)

ans = -1
for i in range(MAX_TIME + 1):
    if dp[i] >= M:
        ans = i
        break
print(ans)