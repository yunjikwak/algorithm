L, len_C = map(int, input().split())
C = list(input().split())

vowel = ['a', 'e', 'i', 'o', 'u']

include = [False for _ in range(len_C)]

result = []

def password(k):
    if include.count(True) == L:
        cnt = 0
        tmp = []
        for i in range(len_C):
            if include[i]:
                tmp.append(C[i])
                if C[i] in vowel:
                    cnt += 1
        if cnt >= 1 and cnt <= L-2:
            tmp.sort()
            tmp = ''.join(tmp)
            result.append(tmp)
            return
    
    if k == len_C:
        return
        
    include[k] = True
    password(k+1)
    include[k] = False
    password(k+1)
    
password(0)
result.sort()
for i in result:
    print(i)