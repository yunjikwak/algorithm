N = int(input())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))

max_cnt = 0
for i in range(N):
    for j in range(N - 2):
        max_cnt = max(max_cnt, maps[i][j] + maps[i][j + 1] + maps[i][j+2])

print(max_cnt)
