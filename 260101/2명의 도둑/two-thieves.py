N, M, C = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

def find_max_val(x, y, idx, cur_w, cur_v):
    if idx == M:
        return cur_v
    
    weight = arr[x][y + idx]
    val = weight ** 2
    
    max_val = find_max_val(x, y, idx + 1, cur_w, cur_v)

    if cur_w + weight <= C:
        max_val = max(max_val, find_max_val(x, y, idx + 1, cur_w + weight, cur_v + val))
    
    return max_val

def calc(select):
    result = 0
    
    for i in range(len(select)):
        x, y = select[i]
        result += find_max_val(x, y, 0, 0, 0)
    
    return result

result = 0
for r1 in range(N):
    for c1 in range(N - M + 1):
        for r2 in range(N):
            for c2 in range(N - M + 1):

                if r1 == r2 and abs(c1 - c2) < M:
                    continue

                val1 = find_max_val(r1, c1, 0, 0, 0)
                val2 = find_max_val(r2, c2, 0, 0, 0)

                result = max(result, val1 + val2)

print(result)