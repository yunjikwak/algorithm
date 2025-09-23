import operator
import sys
input = sys.stdin.readline

string = list(input().strip())
N = len(string)

num = 0
alpha = {}
for ch in string:
    if ch.isalpha() and ch not in alpha:
        num += 1
        alpha[ch] = 0

answer = []
max_answer = float('-inf')

maching = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul
}

def check(answer):
    global max_answer

    idx = 0
    result = None
    op = None
    local_map = {} 

    for ch in string:
        if ch.isalpha():
            if ch not in local_map:
                local_map[ch] = answer[idx]
                idx += 1  
            val = local_map[ch]
            
            if result is None:
                result = val
            else:
                result = maching[op](result, val)
        else:
            op = ch
    max_answer = max(max_answer, result)

def cal(size):
    if size == num:
        check(answer)
        return
    
    for i in range(1, 5):
        answer.append(i)
        cal(size + 1)
        answer.pop()
    
    return

cal(0)
print(max_answer)