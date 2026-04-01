import sys
input = sys.stdin.readline

N = int(input())
H = [int(input()) for _ in range(N)]
start = min(H)
end = max(H)

def countChunk(standard):
    cnt = 0
    isCnt = False
    for h in H:
        if h > standard and not isCnt:
            isCnt = True
            cnt += 1
        elif h <= standard and isCnt:
            isCnt = False
    return cnt


result = 0
for i in range(start, end+1):
    h = countChunk(i)
    result = max(result, h)
print(result)