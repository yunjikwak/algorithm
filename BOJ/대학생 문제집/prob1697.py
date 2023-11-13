# 구글~~
from collections import deque

N, K = map(int, input().split())

dx = [2, 1, -1]
visited = [False] * 110000

def bfs(x):
    q = deque()
    q.append((x, 1))
    visited[x] = True
    
    while q:
        v, level = q.popleft()
        
        for i in range(3):
            if dx[i] == 2:
                nx = v * 2
            else:
                nx = v + dx[i]
            
            if nx < 0 or nx > 100000:
                continue
            if visited[nx] == True:
                continue
            if nx == K:
                return level
            q.append((nx, level+1))
            visited[nx] = True

if N == K:
    print(0)
else:
    print(bfs(N))