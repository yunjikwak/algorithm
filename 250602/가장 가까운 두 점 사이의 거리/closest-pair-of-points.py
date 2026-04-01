N = int(input())
position = []
for _ in range(N):
    position.append(tuple(map(int, input().split())))

ans = 1000*1000
for i in range(N):
    x1, y1 = position[i]
    for j in range(i+1, N):
        x2, y2 = position[j]
        dist2 = (x1 - x2) ** 2 + (y1 - y2) ** 2
        ans = min(ans, dist2)

print(ans)