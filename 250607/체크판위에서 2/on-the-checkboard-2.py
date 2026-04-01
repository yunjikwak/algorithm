R, C = map(int, input().split())
maps = []
for _ in range(R):
    maps.append(list(input().split()))

cnt = 0
start = maps[0][0]

if start != maps[R-1][C-1]:
    for i in range(1, R-1):
        for j in range(1, C-1):
            if maps[i][j] != start:
                for k in range(i+1, R-1):
                    for l in range(j+1, C-1):
                        if maps[k][l] != maps[i][j]:
                                cnt += 1
print(cnt)
