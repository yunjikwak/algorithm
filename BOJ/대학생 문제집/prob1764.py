import sys
input = sys.stdin.readline

N, M = map(int, input().split())
no_listen = []

for _ in range(N):
    no_listen.append(input().rstrip())
no_listen.sort()

def binary_search(target, start, end):
    if start > end:
        return None
    
    mid = (start + end) // 2
    
    if no_listen[mid] == target:
        return mid
    elif no_listen[mid] > target:
        end = mid - 1
    else:
        start = mid + 1
        
    return binary_search(target, start, end)

result = []
for _ in range(M):
    tmp = input().rstrip()
    if binary_search(tmp, 0, N - 1) is not None:
        result.append(tmp)
        
result.sort()
print(len(result))
print(*result, sep='\n')