N = int(input())
arr = []
for i in range(N):
    start, end = map(int, input().split())
    arr.append([start, end])

arr.sort(key=lambda x: (x[1], x[0])) # x[1] 정렬 후 동일 값은 x[0]으로 정렬

cnt = 0
end_point = 0

for i in range(N):
    if arr[i][0] >= end_point:
        cnt += 1
        end_point = arr[i][1]

print(cnt)
