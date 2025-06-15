import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

result = 0
for i in range(N-M+1):
    arr = B[:]
    for j in range(i, i+M):
        if A[j] not in arr:
            break
        else:
            arr.remove(A[j])
    if len(arr) == 0:
        result += 1
print(result)