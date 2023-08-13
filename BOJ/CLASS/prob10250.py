T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())
    a = N // H
    b = N % H
    
    if b == 0:
        if a < 10:
            print(f'{H}0{a}')
        else:
            print(f'{H}{a}')
    elif a < 9:
        print(f'{b}0{a+1}')
    else:
        print(f'{b}{a+1}')
