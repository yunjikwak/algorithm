import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

# H 이상을 하려면 몇 개의 수를 올려야하는가
for h in range(max(arr), min(arr)-1, -1):
    cnt = 0
    up = 0
    for a in arr:
        if a >= h:
            cnt += 1
        elif a+1 == h:
            up += 1
    need = h-cnt
    if need <= 0 or (up >= need and L >= need):
        print(h)
        break