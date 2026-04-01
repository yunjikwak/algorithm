import sys
from collections import Counter
input = sys.stdin.readline

X, Y = map(int, input().split())

def interesting(num):
    num = str(num)
    counts = Counter(num)
    if sorted(counts.values()) == [1, len(num)-1]:
        return True
    return False

result = 0
for i in range(X, Y+1):
    if interesting(i):
        result += 1
print(result)