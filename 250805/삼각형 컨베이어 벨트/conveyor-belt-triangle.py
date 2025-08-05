import sys
input = sys.stdin.readline

N, T = map(int, input().split())
arr = list(map(int, input().split())) + list(map(int, input().split())) + list(map(int, input().split()))

rotate = T % (N*3)
rotated_arr = arr[-rotate:] + arr[:-rotate]

print(*rotated_arr[:N])
print(*rotated_arr[N:N*2])
print(*rotated_arr[N*2:])