import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

N = int(input())
A = list(map(int, input().split()))

min_val = INT_MAX
for i in range(N):
    sum_diff = 0
    for j in range(N):
        sum_diff += abs(i-j)*A[j]
    if sum_diff < min_val:
        min_val = sum_diff
print(min_val)