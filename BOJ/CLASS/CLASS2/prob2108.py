import sys
input = sys.stdin.readline # 안 하면 시간초과

N = int(input())
arr = list(int(input()) for _ in range(N))

mean = sum(arr) / N
print(round(mean))

arr.sort()
median = arr[N // 2]
print(median)

mode = {}
for i in range(N):
    if arr[i] not in mode:
        mode[arr[i]] = 1
    else:
        mode[arr[i]] += 1
# mode = sorted(mode.items(), key=lambda x:-x[1])
max_cnt = max(mode.values())
mode = [k for k, v in mode.items() if max_cnt == v]
print(mode[1] if len(mode) > 1 else mode[0])

print(arr[-1]-arr[0])