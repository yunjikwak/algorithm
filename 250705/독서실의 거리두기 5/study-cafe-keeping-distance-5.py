import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().strip()))

def distance(lst):
    dis = N

    last = -1
    for i in range(len(lst)):
        if lst[i] == 1:
            if last != -1:
                dis = min(dis, i-last)
            last = i
    return dis

result = 0
for i in range(1, N):
    temp_arr = arr[:i] + [1] + arr[i:]
    result = max(result, distance(temp_arr))
print(result)
