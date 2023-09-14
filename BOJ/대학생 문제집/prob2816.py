N = int(input())
arr = [input() for _ in range(N)]

KBS1 = arr.index('KBS1')

now = 0
result = []

if KBS1 != 0:
    while now != KBS1:
        result.append("1")
        now += 1
    while KBS1 != 0:
        result.append("4")
        arr[KBS1] = arr[KBS1-1]
        arr[KBS1-1] = "KBS1"
        KBS1 -= 1
        now -= 1
        
KBS2 = arr.index('KBS2')

if KBS2 != 1:
    if KBS2 == 0:
        result.append("3")
        now += 1
    else:
        while now != KBS2:
            result.append("1")
            now += 1
        for _ in range(KBS2-1):
            result.append("4")
result = ''.join(result)
print(result)