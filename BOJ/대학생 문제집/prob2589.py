from collections import deque

x, y = map(int, input().split())
treasure = []
for i in range(x):
    treasure.append(list(input()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def bfs(a, b, level):
    visited = [[False for _ in range(y)] for _ in range(x)]
    q = deque()
    q.append((a, b, level))
    visited[a][b] = True
	
    while q:
        aa, bb, levl = q.popleft()
        
        for i in range(4):
            nx = aa + dx[i]
            ny = bb + dy[i]
			
            if nx < 0 or nx >= x or ny < 0 or ny >= y:
                continue
            if visited[nx][ny] == True or treasure[nx][ny] == 'W':
                continue
            q.append((nx, ny, levl+1))
            visited[nx][ny] = True
    return levl

result = 0
for i in range(x):
    for j in range(y):
        if treasure[i][j] == 'L':
            tmp = bfs(i, j, 0)
            if result < tmp:
                result = tmp
print(result)