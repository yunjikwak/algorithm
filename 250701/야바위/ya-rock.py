import sys
input = sys.stdin.readline

N = int(input())
act = [list(map(int, input().split())) for _ in range(N)]

max_score, pos = 0, 0
for i in range(1, 4):
    ans, score = i, 0
    for j in range(N):
        a, b, c = act[j]
        if a == ans:
            ans = b
        elif b == ans:
            ans = a
        
        if c == ans:
            score += 1
    if max_score < score:
        max_score = score
        pos = i
print(pos)