N, M = map(int, input().split())

arr = []
for _ in range(N):
    w, v = map(int, input().split())
    arr.append((w, v))

dp = [0] * (M+1)

for w, v in arr:
    for j in range(w, M + 1):
        dp[j] = max(dp[j], dp[j-w] + v)

print(dp[M])