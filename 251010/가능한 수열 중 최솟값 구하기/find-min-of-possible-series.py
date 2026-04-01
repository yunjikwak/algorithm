N = int(input())
arr = []

def check(arr):
    for i in range(1, len(arr)//2+1):
        if arr[-i:] == arr[-i-i:-i]:
            return False
    return True

def bt(num):
    if num == N:
        print(''.join(map(str, arr)))
        return True
        
    for i in range(4, 7):
        arr.append(i)
        if (len(arr) > 1 and arr[-2] == i):
            arr.pop()
            continue
        if not check(arr):
            arr.pop()
            continue
        if bt(num+1):
            return True
        arr.pop()
    return False

bt(0)
# print(arr)