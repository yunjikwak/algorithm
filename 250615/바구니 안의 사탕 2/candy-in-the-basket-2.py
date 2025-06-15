import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 101

for _ in range(N):
    a, b = map(int, input().split())
    arr[b] += a

max_candy = 0
for i in range(101):
    candy = 0
    for j in range(max(0, i - K), min(100, i + K) + 1):
        candy += arr[j]
    max_candy = max(max_candy, candy)
print(max_candy)