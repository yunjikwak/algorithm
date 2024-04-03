N, M, B = map(int, input().split())

ground = []
for _ in range(N):
    ground.extend(list(map(int, input().split())))

ground.sort()
min_height = ground[0]
max_height = ground[-1]

total = float('inf')
height = 0
for i in range(min_height, max_height+1):
    second = 0
    store = B
    lack = 0
    
    for x in ground: # 각 땅의 높이 x
        if x < i: # 기준 높이보다 작으면 추가해야함
            second += i-x
            lack += i-x
        else: # 기준 높이보다 크면 뻬야함
            second += (x-i)*2
            store += (x-i)
    if store < lack:
        continue
    elif (total == second) and (height < i):
        total = second
        height = i
    elif total > second:
        total = second
        height = i
        
print(total, height)