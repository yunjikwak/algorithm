import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))

arr.sort()
first = arr[0] + arr[-1]
second = arr[1] + arr[-2]
third = arr[2] + arr[-3]

max_val = max(first, max(second, third))
min_val = min(first, min(second, third))

print(max_val - min_val)