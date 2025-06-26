import sys
input = sys.stdin.readline

N, M, D, S = map(int, input().split())
ate = [[] for _ in range(N+1)]

for _ in range(D):
    p, m, t = map(int, input().split())
    ate[p].append((m, t))

sick = [list(map(int, input().split())) for _ in range(S)]
store = [0] * (M+1)

for num, timing in sick:    
    for chz, t in ate[num]:
        if t < timing:
            store[chz] += 1

suspect_cheeses = []
for i in range(1, M + 1):
    if store[i] == S:
        suspect_cheeses.append(i)

result = 0

for chz in suspect_cheeses:
    cnt = 0
    for p in range(1, N+1):
        for n, t in ate[p]:
            if n == chz:
                cnt += 1
                break
    result = max(result, cnt)
print(result)