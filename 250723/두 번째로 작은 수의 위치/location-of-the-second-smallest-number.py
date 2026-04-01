import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

arr_sort = sorted(set(arr))
if len(arr_sort) > 1 and arr.count(arr_sort[1]) == 1:
    print(arr.index(arr_sort[1])+1)
else:
    print(-1)