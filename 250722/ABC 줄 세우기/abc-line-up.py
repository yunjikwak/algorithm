import sys
input = sys.stdin.readline

N = int(input())
arr = list(input().split())

result = 0
for i in range(len(arr)):
    for j in range(i, len(arr)):
        if arr[i] > arr[j]:
            result += 1
print(result)