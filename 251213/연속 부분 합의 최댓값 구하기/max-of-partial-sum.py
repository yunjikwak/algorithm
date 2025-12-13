import sys

INT_MIN = -sys.maxsize

N = int(input())
arr = [0] + list(map(int, input().split()))

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = INT_MIN
dp[1] = arr[1]

for i in range(2, N+1):
    dp[i] = max(dp[i-1]+arr[i], arr[i])

ans = INT_MIN
for i in range(1, N+1):
    ans = max(ans, dp[i])

print(ans)