opr_types  = ['+', '-']
a = input()

arr = ''
n = []
opr = []
# 입력 받은 숫자와 연산자 따로 저장
for i in range(len(a)):
    if a[i] in opr_types:
        n.append(int(arr))
        arr = ''
        opr.append(a[i])
    else:
        arr+=a[i]
n.append(int(arr))

# 더하기만 미리 계산
idx = 0
for i in range(len(opr)):
    if opr[i] == opr_types[0]:
        n[idx] += n[idx+1]
        del n[idx+1]
    else:
        idx += 1

# 뺄 수 있으면 빼기
if len(n) > 1 :
    result = n[0]
    for i in range(1, len(n)):
        result -= n[i]
    print(result)
else:
    print(n[0])