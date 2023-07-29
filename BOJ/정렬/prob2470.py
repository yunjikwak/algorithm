N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = len(arr)-1
result = [arr[start], arr[end]]

while start < end :
    tmp = arr[start] + arr[end]
    if tmp == 0 :
        result = [arr[start], arr[end]]
        break
    elif tmp > 0:
        if abs(tmp) < abs(result[0]+result[1]) : # 절대값 비교
            result = [arr[start], arr[end]]
        end -= 1
    elif tmp < 0:
        if abs(tmp) < abs(result[0]+result[1]) :
            result = [arr[start], arr[end]]
        start += 1

print(result[0], result[1])