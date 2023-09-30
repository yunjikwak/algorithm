N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

arr.sort(key = lambda x:(-x[1],-x[2],-x[3]))

result = 1
for row in arr:
    if row[0] == K:
        break
    result += 1
# print(arr, result)
# result = arr[0].index(K) + 1

def check_same(a, b):
    for i in range(1,4):
        if a[i] != b[i]:
            return False
    return True

while result > 1 and check_same(arr[result-1], arr[result-2]):
    # print(result)
    result -= 1

print(result)