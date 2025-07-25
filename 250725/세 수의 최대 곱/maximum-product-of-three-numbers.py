import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

# 양 3 or 양1 음2
# 모두 음 -> 절대값 낮은 것

arr.sort()
result = 0
if arr[0] < 0 and arr[-1] < 0: # 전체 음
    result = arr[0] * arr[1] * arr[2]
else:
    result = max(result, arr[-1]*arr[-2]*arr[-3]) # 양3
    result = max(result, arr[-1]*arr[0]*arr[1])
print(result)