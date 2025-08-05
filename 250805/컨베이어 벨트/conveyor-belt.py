import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = list(map(int, input().split())) + list(map(int, input().split()))

rotate = T % (N*2)
rotated_arr = arr[-rotate:] + arr[:-rotate]

print(*rotated_arr[:N])
print(*rotated_arr[N:])