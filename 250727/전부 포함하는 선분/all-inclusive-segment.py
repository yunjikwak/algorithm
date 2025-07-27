import sys
input = sys.stdin.readline

N = int(input())
arr = list(tuple(map(int, input().split())) for _ in range(N))

a1 = sorted(arr, key=lambda x:x[1])
a2 = sorted(arr, key=lambda x:x[0])

result = a1[-2][1] - a2[0][0]
result = min(result, a1[-1][1] - a2[1][0])

print(result)