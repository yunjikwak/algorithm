from bisect import bisect_left, bisect_right
n = int(input())
N = list(map(int, input().split()))
m = int(input())
M = list(map(int, input().split()))

def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

N.sort() # 정렬하기!!!!!

for i in range(m):
    count = count_by_range(N, M[i], M[i])
    if count == 0:
        print(0)
    else:
        print(1)