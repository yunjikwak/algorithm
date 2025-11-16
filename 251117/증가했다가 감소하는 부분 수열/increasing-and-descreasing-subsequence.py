N = int(input())
arr = list(map(int, input().split()))

dp = [[False, 1] for _ in range(N)]

# for i in range(N):
#     status = dp[i][0]
#     for j in range(i):
#         if status == False:
#             if arr[j] < arr[i]:
#                 dp[i][1] = max(dp[i][1], dp[j]+1)
#             else:
#                 if dp[i][1] < dp[j]+1:
#                     dp[i][0] = True
#                     dp[i][1] = max(dp[i][1], dp[j]+1)
#         else:
#             if arr[j] > arr[i]:
#                 dp[i][1] = max(dp[i], dp[j]+1)

for i in range(N):
    for j in range(i):
        status = dp[j][0]
        
        if status == False:
            if arr[j] < arr[i]:
                dp[i][1] = max(dp[i][1], dp[j][1]+1)
            else:
                if dp[i][1] < dp[j][1]+1:
                    dp[i][0] = True
                    dp[i][1] = max(dp[i][1], dp[j][1]+1)
        else:
            if arr[j] > arr[i]:
                dp[i][1] = max(dp[i][1], dp[j][1] + 1)
                dp[i][0] = True

result = 0
for status, length in dp:
    result = max(result, length)

print(result)