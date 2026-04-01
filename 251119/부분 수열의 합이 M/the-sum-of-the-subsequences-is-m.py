import sys

INT_MAX = sys.maxsize

N, M = map(int, input().split())
arr = list(map(int, input().split()))
dp = [0] * (M+1)

def init():
    for i in range(M+1):
        dp[i] = INT_MAX
    
    dp[0] = 0

init()

for num in arr:
    for j in range(M, num - 1, -1):
        if dp[j - num] != INT_MAX:
            dp[j] = min(dp[j], dp[j - num] + 1)

ans = dp[M]

if ans == INT_MAX:
    ans = -1

print(ans)