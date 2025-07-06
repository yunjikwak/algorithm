import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]


for i in range(1, 11):
    val = i
    check = True
    for j in range(N):
        val *= 2
        a, b = arr[j]
        if a <= val <= b:
            continue
        else:
            check = False
            break
    if check:
        print(i)
        break
    