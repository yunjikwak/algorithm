N, K = map(int, input().split())
cost = []
for _ in range(N):
    cost.append(int(input()))

result = 0
for i in range(N-1, -1, -1):
    if cost[i] > K:
        continue
    else:
        result += K // cost[i]
        K = K % cost[i]
    if K == 0:
        break
print(result)