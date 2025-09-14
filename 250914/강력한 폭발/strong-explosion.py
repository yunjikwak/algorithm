N = int(input())

move = []
move.append([(-2, 0), (-1, 0), (1, 0), (2, 0)])
move.append([(-1, 0), (1, 0), (0, -1), (0, 1)])
move.append([(-1, -1), (-1, 1), (1, -1), (1, 1)])

graph = []
for _ in range(N):
    graph.append(list(map(int, input().split())))

start = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            start.append((i, j))

result = 0
answer = []

def in_range(x, y):
    return 0<=x<N and 0<=y<N

def calc():
    cnt = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for idx, (i, j) in enumerate(start):
        if not visited[i][j]:
            visited[i][j] = True
            cnt += 1

        pattern_idx = answer[idx]
        for dx, dy in move[pattern_idx]:
            nx, ny = i + dx, j + dy
            if in_range(nx, ny) and not visited[nx][ny]:
                cnt += 1
                visited[nx][ny] = True
    return cnt

def recur(num):
    global result

    if num == len(start):
        cur = calc()
        if cur > result:
            result = cur
        return
    
    for select in range(3):
        answer.append(select)
        recur(num+1)
        answer.pop()

    return

recur(0)
print(result)