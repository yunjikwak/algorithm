N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
result = 0
for i in range(N):
    tmp = max(B)
    result += A[i] * tmp
    B.remove(tmp)
print(result)