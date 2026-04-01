import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

result = 0
for i in range(N):
    state = True
    for j in range(N):
        if i == j:
            continue
        a1, a2 = arr[i]
        b1, b2 = arr[j]

        if (a1 < b1 and a2 > b2) or (a1 > b1 and a2 < b2):
            state = False
            break
            
    if state:
        result += 1
print(result)
        