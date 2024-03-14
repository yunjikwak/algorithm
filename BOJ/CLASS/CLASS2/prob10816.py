from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
count_arr = list(map(int, input().split()))

cnt = Counter(arr)

for i in range(M):
    if count_arr[i] in cnt:
        print(cnt[count_arr[i]], end = ' ')
    else:
        print(0, end = ' ')
