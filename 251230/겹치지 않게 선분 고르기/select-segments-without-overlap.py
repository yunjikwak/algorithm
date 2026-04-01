N = int(input())

lines = []
for _ in range(N):
    l, r = map(int, input().split())
    lines.append((l, r))

def is_overlap(arr):
    tmp = [0] * 1002
    
    for i in range(len(arr)):
        l, r = arr[i]
        
        for k in range(l, r+1):
            if tmp[k] == 0:
                tmp[k] += 1
            else:
                return True
        
    return False

arr = []
answer = 0

def back(idx):
    global answer

    if is_overlap(arr):
        return
    
    if idx == N:
        answer = max(answer, len(arr))
        return

    arr.append(lines[idx])
    back(idx + 1)
    arr.pop()
    back(idx + 1)

back(0)
print(answer)