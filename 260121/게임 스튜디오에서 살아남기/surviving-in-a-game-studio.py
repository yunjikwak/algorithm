N = int(input())
offset = 10**9 + 7

dp = [[[0] * 3 for _ in range(3)] for _ in range(N + 1)]
dp[0][0][0] = 1

for i in range(N):
    for t in range(3):
        for b in range(3):
            dp[i+1][t][0] = (dp[i+1][t][0] + dp[i][t][b]) % offset

            if t+1 < 3:
                dp[i+1][t+1][0] = (dp[i+1][t+1][0] + dp[i][t][b]) % offset
            
            if b+1 < 3:
                dp[i+1][t][b+1] = (dp[i+1][t][b+1] + dp[i][t][b]) % offset

result = 0
for t in range(3):
    for b in range(3):
        result = (result + dp[N][t][b]) % offset

print(result)