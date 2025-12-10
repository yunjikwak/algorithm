N = int(input())
arr = list(map(int, input().split()))

dp = [-1] * (2*100*1000 + 1) # (인덱스 i에 해당하는 차이)를 만들었을 때, 가능한 A 그룹 합의 최댓값
dp[100*1000] = 0

for num in arr:
    next_dp = dp[:] 
    for i in range(len(dp)):
        if dp[i] == -1: 
            continue
        if i + num < len(dp):
            next_dp[i + num] = max(next_dp[i + num], dp[i] + num)
        if i - num >= 0:
            next_dp[i - num] = max(next_dp[i - num], dp[i])
    dp = next_dp

print(dp[100*1000])