# pypy로 통과 python 시간초과

N = int(input())
arr = []
for _ in range(N):
    arr.append(int(input()))
arr.sort()

def roundFive(x):
    if (x - int(x)) >= 0.5:
        return int(x)+1
    else:
        return int(x)

remove = roundFive(N*0.15)
arr = arr[remove:N-remove]

if len(arr):
    print(roundFive((sum(arr[:])/len(arr))))
else:
    print(0)
    
"""
파이썬 오사오입
.5인 경우 5 앞자리가 홀 -> 올림, 짝 -> 내림

사사오입으로 바꿔야함
"""