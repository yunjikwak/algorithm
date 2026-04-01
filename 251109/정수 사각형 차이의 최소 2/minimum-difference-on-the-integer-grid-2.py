from collections import deque
import sys
sys.setrecursionlimit(250000)

input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]

dirs = [(1, 0), (0, 1)]

def bfs(low, high):
    if not (low <= grid[0][0] <= high):
        return False
    visited = [[False]*N for _ in range(N)]
    q = deque([(0, 0)])
    visited[0][0] = True

    while q:
        x, y = q.popleft()

        if x == N-1 and y == N-1:
            return True

        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if low <= grid[nx][ny] <= high:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return False

answer = 100

for low in range(1, 101):
    for high in range(low, 101):
        if bfs(low, high):
            answer = min(answer, high - low)
            break

print(answer)
