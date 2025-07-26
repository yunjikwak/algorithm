import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

## 짝홀
# 짝 - 짝 짝짝 홀홀 짝홀홀
# 홀 -홀 짝짝홀 홀홀홀

even_cnt = 0
odd_cnt = 0
for i in range(N):
    if arr[i] % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

if even_cnt == odd_cnt:
    print(even_cnt*2)
elif even_cnt > odd_cnt:
    print(odd_cnt + 1)
else:
    result = even_cnt * 2
    odd_cnt -= even_cnt
    
    quotient = odd_cnt // 3
    remainder = odd_cnt % 3 

    if remainder == 0:
        result += 2*quotient
    elif remainder == 1:
        result += 2*quotient-1
    elif remainder == 2:
        result += 2*quotient+1

    print(result)