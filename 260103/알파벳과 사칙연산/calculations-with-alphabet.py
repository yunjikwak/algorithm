arr = list(input().strip())

alpha = []
for ch in arr:
    if 'a' <= ch <= 'f':
        if ch not in alpha:
            alpha.append(ch)
alpha.sort()

def calc(expr, cur_map):
    cur_val = cur_map[expr[0]]
    
    for i in range(1, len(expr), 2):
        op = expr[i]
        next_val = cur_map[expr[i+1]] 
        
        if op == '+':
            cur_val += next_val
        elif op == '-':
            cur_val -= next_val
        elif op == '*':
            cur_val *= next_val
            
    return cur_val

mapping = {}
result = -float('inf')
def back(idx):
    global result
    
    if idx == len(alpha):
        result = max(result, calc(arr, mapping))
        return
    
    ch = alpha[idx]
    for i in range(1, 5):
        mapping[ch] = i
        back(idx+1)
    
back(0)
print(result)