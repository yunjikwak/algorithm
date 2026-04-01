import sys
input = sys.stdin.readline

N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]

a,b = arr[0]
start = a//2
end = b//2 + 1

for i in range(start, end):
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
    