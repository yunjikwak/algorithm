import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

cnt = 1
for i in range(len(arr)-1, 0, -1):
    if arr[i] > arr[i-1]:
        cnt += 1
    else:
        break
print(len(arr)-cnt)