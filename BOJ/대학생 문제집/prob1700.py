from collections import deque

N, K = map(int, input().split()) # 멀티탭, 사용횟수
schedule = deque(map(int, input().split()))

cur_list = []
result = 0

while schedule:
    next_num = schedule.popleft()
    if next_num in cur_list:
        continue
    
    if len(cur_list) < N:
        cur_list.append(next_num)
    else:
        result += 1
        change_idx = -1
        max_idx = -1
        for i, check in enumerate(cur_list):
            if check not in schedule:
                change_idx = i
                break
            else:
                cur_idx = schedule.index(check)
                if cur_idx > max_idx:
                    max_idx = cur_idx
                    change_idx = i
        cur_list[change_idx] = next_num
                
print(result)