N = int(input())

def is_beautiful(num):
    idx = 0
    cnt = num[idx]
    cur_num = 1

    while idx < len(num):
        if idx+1 == len(num):
            if cnt == cur_num:
                return True
            else:
                return False

        if cnt != num[idx+1]: # 새로운 수 등장
            if cnt != cur_num: # 연속 만족 안함
                return False
            else: # 업데이트
                idx += 1
                cnt = num[idx]
                cur_num = 1
        else: # 동일 수 연속
            if cur_num+1 > cnt: # 횟수 초과
                cur_num = 1 # 리셋
            else:
                cur_num += 1
            idx += 1

result = 0
arr = []

def back(cur_idx):
    global result
    
    if cur_idx == N:
        if is_beautiful(arr):
            result += 1
        return
    
    for i in range(1, 5):
        arr.append(i)
        back(cur_idx+1)
        arr.pop()
    return

back(0)
print(result)