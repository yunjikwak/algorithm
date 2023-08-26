# Python3 -> 시간 초과
# PyPy3 ok
from collections import deque

N, M = map(int, input().split())
indegree = [0] * (N + 1)
graph = [[] for i in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B) # A가 먼저 와야함 A -> B
    indegree[B] += 1

def topology_sort():
    result = []
    q = deque()
    for i in range(1, N + 1):
        if indegree[i] == 0:
            q.append(i)
            
    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)
    for i in result:
        print(i, end=' ')

topology_sort()