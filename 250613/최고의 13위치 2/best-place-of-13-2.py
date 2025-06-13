import sys
input = sys.stdin.readline

N = int(input())
maps = []

for _ in range(N):
    maps.append(list(map(int, input().split())))

block = []
for i in range(N):
    for j in range(N-2):
        cur = maps[i][j] + maps[i][j+1] + maps[i][j+2]
        block.append((cur, i, j))

result = 0
for i in range(len(block)):
    for j in range(i+1, len(block)):
        val1, x1, y1 = block[i]
        val2, x2, y2 = block[j]

        if x1 == x2 and not (y1+2 < y2 or y2+2 < y1):
            continue
        
        if result < val1+val2:
            result = val1 + val2
print(result)