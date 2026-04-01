N, M, C = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

def get_max_val(arr):
    max_val = 0
    
    def recur(idx, cur_sum, val):
        nonlocal max_val #  나를 감싸고 있는 가장 가까운 바깥 함수

        if cur_sum > C:
            return
        
        if idx == M:
            max_val = max(max_val, val)
            return

        recur(idx + 1, cur_sum, val)
        select = arr[idx]
        recur(idx + 1, cur_sum + select, val + select**2)

    recur(0, 0, 0)
    return max_val

max_arr = [[0] * (N - M + 1) for _ in range(N)]
for r in range(N):
    for c in range(N - M + 1):
        block = arr[r][c : c + M]
        max_arr[r][c] = get_max_val(block)

result = 0
for x in range(N):
    for y in range(N - M + 1):
        for x2 in range(x, N):
            if x == x2:
                start = y + M
            else:
                start = 0
            for c2 in range(start, N - M + 1):
                val1 = max_arr[x][y]
                val2 = max_arr[x2][c2]
                result = max(result, val1 + val2)
print(result)