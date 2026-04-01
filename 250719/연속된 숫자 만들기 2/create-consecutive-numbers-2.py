import sys
input = sys.stdin.readline

pos = list(map(int, input().split()))
pos.sort()

def check(arr):
    seq = []
    for i in range(len(arr)-1):
        seq.append(arr[i+1] - arr[i])
    seq.sort()
    if seq[-1] == 1:
        return 0
    elif seq[-1] > 1:
        for s in seq:
            if s == 2:
                return 1
        return 2

print(check(pos))