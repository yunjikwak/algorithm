import sys
input = sys.stdin.readline

N = int(input())
arr = [(-1, -1)] * 11

result = 0
for _ in range(N):
    num, direction = map(int, input().split())
    before_d, cross = arr[num]
    if before_d == -1:
        arr[num] = (direction, 0)
    else:
        before_d, cross = arr[num]
        if before_d != direction:
            arr[num] = (direction, cross+1)
            result += 1
print(result)