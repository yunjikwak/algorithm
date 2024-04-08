import sys
input = sys.stdin.readline

# 구간 합 -> Prefix Sum
N, M = map(int, input().split())
arr = list(map(int, input().split()))

sum_value = 0
prefix_sum = [0] # index 맞추기용
for i in arr:
    sum_value += i
    prefix_sum.append(sum_value)

for _ in range(M):
    a, b = map(int, input().split())
    print(prefix_sum[b] - prefix_sum[a-1])