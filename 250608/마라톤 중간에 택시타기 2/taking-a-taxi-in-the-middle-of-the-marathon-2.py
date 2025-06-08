import sys

input = sys.stdin.readline
INT_MAX = sys.maxsize

N = int(input())
dist = []

for _ in range(N):
    x, y = map(int, input().split())
    dist.append((x, y))

total_dist = 0
for i in range(N-1):
    total_dist += abs(dist[i][0] - dist[i+1][0]) + abs(dist[i][1] - dist[i+1][1])

min_dist = INT_MAX
for i in range(1, N-1):
    sum_dist = total_dist
    sum_dist -= abs(dist[i-1][0] - dist[i][0]) + abs(dist[i-1][1] - dist[i][1])
    sum_dist -= abs(dist[i][0] - dist[i+1][0]) + abs(dist[i][1] - dist[i+1][1])
    sum_dist += abs(dist[i-1][0] - dist[i+1][0]) + abs(dist[i-1][1] - dist[i+1][1])

    if sum_dist < min_dist:
        min_dist = sum_dist

print(min_dist)