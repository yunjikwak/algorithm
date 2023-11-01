from collections import deque
import sys
input = sys.stdin.readline

M, N, K = map(int, input().split()) # 5 7
arr = [ [False] * N for _ in range(M)]

for _ in range(K):
    left_x, left_y, right_x, right_y = map(int, input().split()) # 0 2 4 4
    left_y = M - left_y - 1
    right_x -= 1
    right_y = M - right_y
    
    for i in range(right_y, left_y+1):
        for j in range(left_x, right_x+1):
            arr[i][j] = True
    # 0 2 -> [2, 0] [left_y, left_x]
    # 4 4 -> [1, 3] [right_y, right_x]
    # 1 1 [0, 1] -> [left_y, left_x]
    # 2 5 [3, 1] -> [right_y, right_x]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
visited  = [[False] * N for _ in range(M)]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    
    cnt = 1
    
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if visited[nx][ny] == True or arr[nx][ny] == True:
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
            cnt += 1
    return cnt

result = []
for i in range(M):
    for j in range(N):
        if visited[i][j] == False and arr[i][j] == False:
            result.append(bfs(i, j))
result.sort()
print(len(result))
print(*result, end =' ')