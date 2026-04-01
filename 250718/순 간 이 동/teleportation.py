import sys
input = sys.stdin.readline

A, B, x, y = map(int, input().split())

min_dis = abs(A-B)
min_dis = min(abs(A-x)+abs(B-y), min_dis)
min_dis = min(abs(A-y)+abs(B-x), min_dis)

print(min_dis)