import sys
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    a, b = input().split()
    arr.append((int(a), b))

arr.sort(key = lambda x:x[0])

result = 0
for i in range(len(arr)):
    start, end = arr[i][0] , arr[i][0]
    last = arr[i][1]
    cnt = 1

    for j in range(i+1, len(arr)):
        if arr[j][1] != last:
            break
        end = arr[j][0]
    cnt = end - start
    
    result = max(result, cnt)

for i in range(len(arr)):
    cntG = 0
    cntH = 0
    start, end = arr[i][0], arr[i][0]
    for j in range(i, len(arr)):
        if arr[j][1] == 'G':
            cntG += 1
        elif arr[j][1] == 'H':
            cntH += 1
        if cntG == cntH:
            end = arr[j][0]
    cnt = end - start

    result = max(result, cnt)

print(result)