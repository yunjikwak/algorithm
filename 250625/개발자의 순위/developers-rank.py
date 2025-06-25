K, N = map(int, input().split())

arr = [] * (N+1)
for _ in range(N):
    lst = list(map(int, input().split()))
    for i in range(N):
        arr[lst[i]].append(i+1)

print(arr)

# for i in range(N):
#     for j in range(N):
#         if 
            