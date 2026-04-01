from collections import deque

N, M = map(int, input().split())

skill = {}
for _ in range(N):
    x, y = map(int, input().split())
    skill[x] = y

for _ in range(M):
    u, v = map(int, input().split())
    skill[u] = v

visited = [101] * 101


def bfs():
    queue = deque()
    queue.append((1, 0))

    while queue:
        cur, time = queue.popleft()
        for i in range(1, 7):
            ncur = cur + i
            if ncur in skill:
                ncur = skill[ncur]

            if ncur > 100:
                continue
            if time + 1 < visited[ncur]:
                visited[ncur] = time + 1
                queue.append((ncur, time+1))
    return visited[100]


print(bfs())
