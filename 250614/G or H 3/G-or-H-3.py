import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 10001
for _ in range(N):
    a, b = input().split()
    arr[int(a)] = b

max_score = 0
for i in range(1, 10000 - K):
    score = 0
    for j in range(i, i+K+1):
        if arr[j] == 'G':
            score += 1
        elif arr[j] == 'H':
            score += 2
    max_score = max(max_score, score)
print(max_score)
