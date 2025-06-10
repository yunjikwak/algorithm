import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

result = 0
for i in range(len(A)):
    for j in range(i+2, len(A)):
        if A[i] + A[j] > result:
            result = A[i] + A[j]

print(result)