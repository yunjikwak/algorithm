N = int(input())
result = 0
answer = []

def is_beautiful():
    i = 0
    while i < N:
        # print(answer, i, answer[i])
        target = answer[i]
        if i + target > N:
            return False

        for k in range(i+1, i+target):
            if answer[k] != target:
                return False
        i += target
    return True

def recur(num):
    global result

    if num == N:
        if is_beautiful():
            # print(answer)
            result += 1
        return
    
    for select in range(1, 5):
        answer.append(select)
        recur(num+1)
        answer.pop()

    return

recur(0)
print(result)