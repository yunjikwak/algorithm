import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

result = 0
# first
for i in range(N-1):
    for j in range(M-1):
        cur_sum = 0
        min_val = 1000
        for k in range(2):
            a, b = graph[i+k][j:j+2]
            min_val = min(min_val, a, b)
            cur_sum += a + b
        cur_sum -= min_val
        result = max(result, cur_sum)

# second
# ---
for i in range(N):
    cur_sum = 0
    for j in range(M-2):
        cur_sum = sum(graph[i][j:j+3])
    result = max(result, cur_sum)

# |
# |
# |

for i in range(M):
    for j in range(N-2):
        cur_sum = 0
        for k in range(3):
            cur_sum += graph[j+k][i]
        result = max(result, cur_sum)

print(result)