from itertools import combinations

N, M = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]

def simulate(N, lines):
    mapping = list(range(1, N+1))
    for x, _ in sorted(lines):
        mapping[x-1], mapping[x] = mapping[x], mapping[x-1]
    return mapping


target = simulate(N, lines)

answer = M
for k in range(1, M+1):
    for comb in combinations(lines, k):
        if simulate(N, comb) == target:
            answer = k
            break
    if answer != M:
        break
print(answer)