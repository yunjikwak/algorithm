N = int(input())

work = []
for _ in range(N):
    work.append(list(map(int, input().split())))

max_time = 0
for i in range(N):
    arr = [0] * 1001
    for j in range(N):
        if i == j:
            continue
        a, b = work[j]
        for k in range(a, b):
            arr[k] = 1

    max_time = max(max_time, sum(arr))
print(max_time)