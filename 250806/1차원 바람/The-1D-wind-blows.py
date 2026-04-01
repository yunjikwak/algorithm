import sys
input = sys.stdin.readline

N, M, Q = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]
blow = list(tuple(input().split()) for _ in range(Q))
direction = ['L', 'R']

def is_equal(arr1, arr2):
    for i in range(M):
        if arr1[i] == arr2[i]:
            return True
    return False

def shift(_dir, arr):
    if _dir == 'L':
        return [arr[-1]]+arr[0:M-1]
    else:
        return arr[1:]+[arr[0]]

for col, d in blow:
    cur = int(col)-1
    cur_d = 0
    graph[cur] = shift(d, graph[cur])

    if d == 'L':
        cur_d = 0
    else:
        cur_d = 1

    down_d = cur_d
    for i in range(cur+1, N):
        if is_equal(graph[i-1], graph[i]):
            down_d += 1
            down_d %= 2
            graph[i] = shift(direction[down_d], graph[i])
        else:
            break

    up_d = cur_d
    for i in range(cur-1, -1, -1):
        if is_equal(graph[i+1], graph[i]):
            up_d += 1
            up_d %= 2
            graph[i] = shift(direction[up_d], graph[i])
        else:
            break

for row in graph:
    print(*row)