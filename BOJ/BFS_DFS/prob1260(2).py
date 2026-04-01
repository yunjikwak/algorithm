"""
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오. 단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
"""
# 기본 dfs + bfs

import sys
sys.setrecursionlimit(10000)
from collections import deque

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# sort
for i in range(1, N+1):
    graph[i].sort()

visited_d = [False for _ in range(N+1)]
visited_b = [False for _ in range(N+1)]

def dfs(v):
    visited_d[v] = True
    print(v, end=' ')

    for i in graph[v]:
        if not visited_d[i]:
            dfs(i)

def bfs(start):
    queue = deque([start])
    visited_b[start] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not visited_b[i]:
                queue.append(i)
                visited_b[i] = True

dfs(V)
print()
bfs(V)