from collections import deque

N, M = map(int, input().split())
board = []
queue = deque()

for i in range(N):
    row = list(input().strip())
    for j in range(len(row)):
        if row[j] == "I":
            queue.append((i, j))

    board.append(row)  # O 빈공간, X 벽, P 사람

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def bfs():
    visited = [[False]*M for _ in range(N)]
    count = 0

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        if board[x][y] == 'P':
            count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M or visited[nx][ny] == True or board[nx][ny] == 'X':
                continue
            queue.append((nx, ny))
            visited[nx][ny] = True
    return count


cnt = bfs()
if cnt == 0:
    print("TT")
else:
    print(cnt)
