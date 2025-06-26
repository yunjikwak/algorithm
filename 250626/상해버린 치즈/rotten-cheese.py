import sys
input = sys.stdin.readline

N, M, D, S = map(int, input().split())
ate = [[] for _ in range(N+1)]

for _ in range(D):
    p, m, t = map(int, input().split())
    ate[p].append((m, t))

for i in range(len(ate)):
    ate[i] = sorted(ate[i], key=lambda x: x[1])

sick = [list(map(int, input().split())) for _ in range(S)]
store = [0] * (M+1)

for i in range(len(sick)):
    num = sick[i][0]
    timing = sick[i][1]
    
    for chz, t in ate[num]:
        if t < timing:
            store[chz] += 1

result = 0

for chz in range(1, M+1):
    if store[chz] == len(sick):
        cnt = 0
        for i in range(1, N+1):
            for cheese, _ in ate[i]:
                if cheese == chz:
                    cnt += 1
                    break
        result = max(result, cnt)
    
print(result)