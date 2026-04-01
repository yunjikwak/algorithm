import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
# line = [0] * 102
# arr = []

result = 0
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            line = [0] * 102
            check = True
            for idx in range(len(arr)):
                if idx == i or idx == j or idx == k:
                    continue
                a, b = arr[idx]

                for c in range(a, b+1):
                    if line[c] != 0:
                        check = False
                        break
                    else:
                        line[c] += 1
                
            if check:
                result += 1

print(result)

# for _ in range(N):
#     a, b = map(int, input().split())
#     for i in range(a, b+1):
