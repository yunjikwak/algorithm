arr = list(input().strip())

def calc(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b

def calc_all(nums):
    cur = nums[0]
    ch = arr[1]
    idx = 2

    for i in range(idx, len(arr)):
        if i % 2 == 0: # 홀수
            cur = calc(cur, nums[i], ch)
        else:
            ch = arr[i]
    
    return cur


select = []
result = 0
def back(idx):
    global result
    
    if idx == len(arr):
        result = max(result, calc_all(select))
        return
    
    for i in range(1, 5):
        select.append(i)
        back(idx+1)
        select.pop()
    
back(0)
print(result)