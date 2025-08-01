import sys
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(N)]

def is_valid(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    else:
        return True

def search(K, x, y):
    gold_cnt = 0

    for i in range(x-K, x+K+1):
        for j in range(y-K, y+K+1):
            if is_valid(i, j) and abs(x-i) + abs(y-j) <= K:
                if graph[i][j] == 1:
                    gold_cnt += 1
    
    return gold_cnt

max_gold = 0
for k in range(N//2+2):
    cost = k*k + (k+1)*(k+1)
    for i in range(N):
        for j in range(N):
            ans = search(k,i,j)
            if ans*M >= cost:
                max_gold = max(max_gold, ans)

print(max_gold)
