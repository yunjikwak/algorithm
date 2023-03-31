N = int(input())

def Hanoi(n, start, dest, temp):
    if n == 1:
        print(start, dest)
    else:
        Hanoi(n-1, start, temp, dest)
        print(start, dest)
        Hanoi(n-1, temp, dest, start)

print(2 ** N - 1) # 이동 횟수 -> cnt로 못하나..
if N <= 20:
    Hanoi(N, 1, 3, 2)