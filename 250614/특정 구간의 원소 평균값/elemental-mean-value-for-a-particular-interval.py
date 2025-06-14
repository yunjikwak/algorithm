import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(N):
    for j in range(i, N):
        mean = sum(arr[i:j+1]) / (j+1-i)
        for k in range(i, j+1):
            if mean == arr[k]:
                result += 1
                break
print(result)