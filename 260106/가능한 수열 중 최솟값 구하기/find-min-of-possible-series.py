N = int(input())

result = []

def can():
    for i in range(1, len(result)//2+1):
        if result[-i:] == result[-i-i:-i]:
            return False
    return True
    

def bt():
    if not can():
        return False

    if len(result) == N:
        print(''.join(map(str, result)))
        return True
    
    for i in range(4, 7):
        result.append(i)
        if bt():
            return True
        result.pop()
    return False

bt()