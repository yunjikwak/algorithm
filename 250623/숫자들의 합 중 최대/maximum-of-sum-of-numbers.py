X, Y = map(int, input().split())

max_val = 0
for i in range(X, Y+1):
    num = str(i)
    sum_num = 0
    for k in range(len(num)):
        sum_num += int(num[k])
    
    max_val = max(max_val, sum_num)
print(max_val)