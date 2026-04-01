A = list(input().strip())
cnt = 0
LENGH = len(A)

cnt = 0
startIdx = 0

for i in range(LENGH):
    isOpen = False
    for j in range(startIdx, LENGH):
        if not isOpen and  A[j] == '(':
            startIdx = j + 1
            isOpen = True
        elif isOpen and A[j] == ')':
            cnt += 1

print(cnt)