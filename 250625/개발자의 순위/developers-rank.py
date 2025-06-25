K, N = map(int, input().split())

arr = [[] for _ in range(N+1)]
for _ in range(K):
    lst = list(map(int, input().split()))
    for i in range(N):
        arr[lst[i]].append(i+1)

result = 0
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            continue
        upper = True
        for k in range(K):
            if arr[i][k] < arr[j][k]:
                upper = False
                break
        if upper:
            result += 1

print(result)