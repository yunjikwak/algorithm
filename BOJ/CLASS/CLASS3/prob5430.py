import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    p = input()
    n = int(input())
    arr = input().strip()

    if arr == "[]":
        arr = []
    else:
        arr = list(map(int, arr.strip("[]").split(",")))

    reverse = False

    for i in p:
        if i == 'R':
            reverse = not reverse
        elif i == 'D':
            if len(arr) <= 0:
                print("error")
                break
            if reverse:
                arr.pop()
            else:
                arr.pop(0)

    else:  # for 루프가 break 없이 실행된 경우 실행
        if reverse:
            arr.reverse()
        print(f"[{','.join(map(str, arr))}]")
