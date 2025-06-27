import sys
input = sys.stdin.readline

N, K = map(int, input().split())
bomb = list(int(input().strip()) for _ in range(N))

result = -1
for i in range(N):
    num = bomb[i]
    check = False
    for j in range(1, K+1):
        if i+j >= N:
            break
        elif num == bomb[i+j]:
            check = True
            break
    
    if check:
        result = max(result, num)

print(result)