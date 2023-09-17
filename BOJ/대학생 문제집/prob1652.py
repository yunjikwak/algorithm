N = int(input())
arr = [list(input()) for _ in range(N)]

row_cnt = 0
col_cnt = 0

for row in arr:
    arr_slice = ''.join(row).split('X')
    for x in arr_slice:
        if len(x) >= 2:
            row_cnt += 1

for i in range(N):
    col = [row[i] for row in arr]
    col_slice = ''.join(col).split('X')
    
    for y in col_slice:
        if len(y) >= 2:
            col_cnt += 1

print(row_cnt)
print(col_cnt)