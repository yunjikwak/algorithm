import sys
input = sys.stdin.readline

x1,x2,x3,x4 = map(int, input().split())

if (x1 < x3 and x2 < x3) or (x3 < x1 and x4 < x1):
    print("nonintersecting")
else:
    print("intersecting")