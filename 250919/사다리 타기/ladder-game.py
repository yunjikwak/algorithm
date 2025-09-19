from itertools import combinations

N, M = map(int, input().split())
lines = [tuple(map(int, input().split())) for _ in range(M)]

def simulate(N, lines):
    mapping = list(range(1, N+1))
    for x, _ in sorted(lines, key=lambda line: line[1]):
        mapping[x-1], mapping[x] = mapping[x], mapping[x-1]
    return mapping

target = simulate(N, lines)
# print(target)

answer = M

def recur(num, arr):
    global answer

    if num == M:
        if target == simulate(N, arr):
            answer = min(answer, len(arr))
        return
    
    arr.append(lines[num])
    recur(num+1, arr)
    arr.pop()
    recur(num+1, arr)

    return

recur(0, [])    
print(answer)