import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [0] * 10000
end = 0
for _ in range(N):
    a, b = input().split()
    arr[int(a)] = b
    if int(a) > end:
        end = int(a)

max_score = 0
for i in range(1, end+1):
    score = 0
    for j in range(i, i+K+1):
        if arr[j] == 'G':
            score += 1
        elif arr[j] == 'H':
            score += 2
    max_score = max(max_score, score)
print(max_score)
