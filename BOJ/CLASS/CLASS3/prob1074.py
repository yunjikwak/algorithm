N, r, c = map(int, input().split())

result = 0


def quarter_sum(n, a, b, cal):
    if n == 0:
        return cal
    else:
        x, y = 0, 0
        # 쪼개기
        if a >= pow(2, n-1):
            x = 1
        if b >= pow(2, n-1):
            y = 1
        # result 계산
        cal += (x*2+y)*pow(4, (n-1))
        # 다음값 계산
        if x == 1:
            a = a - (pow(2, n-1))
        if y == 1:
            b = b - (pow(2, n-1))
        # 재귀호출 (return 없이 호출하면 none타입 반환함!)
        return quarter_sum(n-1, a, b, cal)


print(quarter_sum(N, r, c, 0))
