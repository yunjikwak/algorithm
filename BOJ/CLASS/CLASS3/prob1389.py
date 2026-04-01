from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(G, start, visit):
    queue = deque([(start, 0)])
    visit[start] = True
    kbacon = 0

    while queue:
        v, lv = queue.popleft()

        for i in G[v]:
            if not visit[i]:
                queue.append((i, lv+1))
                visit[i] = True
                kbacon += (lv+1)

    return kbacon


min_kbacon = float('inf')  # 무한대 설정
result = 0
for i in range(1, N+1):
    visited = [False] * (N+1)
    now = bfs(graph, i, visited)
    if now < min_kbacon:
        result = i
        min_kbacon = now

print(result)
