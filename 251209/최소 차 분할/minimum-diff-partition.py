N = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
dp = [False] * (total + 1)

dp[0] = True

for i in range(N):
    for j in range(total, arr[i]-1, -1):
        if dp[j-arr[i]]:
            dp[j] = True

min_diff = total
for i in range(total):
    if dp[i]:
        diff = abs(total - 2 * i)
        min_diff = min(min_diff, diff)

print(min_diff)