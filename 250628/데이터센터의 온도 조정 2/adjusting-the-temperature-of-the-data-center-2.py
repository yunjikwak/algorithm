import sys
input = sys.stdin.readline

N, C, G, H = map(int, input().split())
arr = []

start = sys.maxsize
end = -sys.maxsize

for _ in range(N):
    a,b = map(int, input().split())
    start = min(start, a)
    end = max(end, b)
    arr.append((a,b))

def get_work(temp, electro):
    T_a, T_b = arr[electro]
    if temp < T_a:
        return C
    elif temp >= T_a and temp <= T_b:
        return G
    elif temp > T_b:
        return H

result = 0
for i in range(start-1, end+1):
    sum_work = 0
    for n in range(N):
        work = get_work(i, n)
        sum_work += work
    result = max(result, sum_work)
print(result)