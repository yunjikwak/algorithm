N = int(input())
arr = []

for _ in range(N) :
    arr.append(list(map(int, input().split())))
    
# print(array)

# d = [0] * N
# idx = []
# # print(arr[1].index(min(arr[1])))

# d[0] = min(arr[0][0], arr[0][1], arr[0][2])
# idx[0] = arr[0].index(d[0])

# d[1] = min(arr[1][0], arr[1][1], arr[1][2])
# idx[1] = arr[1].index(d[1])

# if idx[0] == idx[1]:
#     if d[0] > d[1]:
#         a = arr[0][:idx[0]] + arr[0][idx[0]+1:]
#         d[0] = min(a)

# for i in range(1, N):
#     d[i] = min(arr[0][0], arr[0][1], arr[0][2])
#     tmp = arr[i].index(d[i])
    
#     if idx == tmp:
#         if d[i] > d[i-1]:
            



for i in range(1, N):
    arr[i][0] = min(arr[i-1][1], arr[i-1][2]) + arr[i][0]
    arr[i][1] = min(arr[i-1][0], arr[i-1][2]) + arr[i][1]
    arr[i][2] = min(arr[i-1][0], arr[i-1][1]) + arr[i][2]
    
print(min(arr[N-1][0],arr[N-1][1],arr[N-1][2]))