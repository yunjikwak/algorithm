import sys
input = sys.stdin.readline

pos = list(map(int, input().split()))

dif_ab = pos[1]-pos[0]-1
dif_bc = pos[2]-pos[1]-1

print(max(dif_ab, dif_bc))