N = int(input())
position = []
for _ in range(N):
    position.append(tuple(map(int, input().split())))

ans = 40000 * 40000
for i in range(N):
    max_width = 0
    min_width = 40000
    max_height = 0
    min_height = 40000

    for j in range(N):
        if i == j:
            continue
        
        x, y = position[j]
        max_width = max(max_height, x)
        min_width = min(min_height, x)
        max_height = max(max_height, y)
        min_height = min(min_height, y)
    
    ans = min(ans, (max_width - min_width) * (max_height - min_height))
print(ans)
