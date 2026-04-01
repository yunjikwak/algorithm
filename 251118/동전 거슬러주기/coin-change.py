import sys

INT_MAX = sys.maxsize

N, M = map(int, input().split())
coin = [0] + list(map(int, input().split()))
dp = [0] * (M+1)

def init():
    for i in range(M+1):
        dp[i] = INT_MAX
    
    dp[0] = 0

init()

for i in range(1, M+1):
    for j in range(1, N+1):
        if i >= coin[j]:
            if dp[i-coin[j]] == INT_MAX:
                continue
            dp[i] = min(dp[i], dp[i - coin[j]] + 1)

ans = dp[M]

if ans == INT_MAX:
    ans = -1

print(ans)