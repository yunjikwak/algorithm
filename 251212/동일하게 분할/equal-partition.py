N = int(input())
arr = list(map(int, input().split()))

total = sum(arr)
dp = [False] * (total + 1)

dp[0] = True

for i in range(N):
    for j in range(total, arr[i]-1, -1):
        if dp[j-arr[i]]:
            dp[j] = True

if total % 2 != 0:
    print("No")
elif dp[total//2]:
    print("Yes")
else:
    print("No")