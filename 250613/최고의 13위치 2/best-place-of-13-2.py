import sys
input = sys.stdin.readline

N = int(input())
maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

first = -1
second = -1
for i in range(N):
    for j in range(N-2):
        cur = maps[i][j] + maps[i][j+1] + maps[i][j+2]
        if first == -1:
            first = cur
        elif second == -1:
            second = cur
        elif cur > first:
            first = cur
        elif cur > second:
            second = cur
print(first + second)