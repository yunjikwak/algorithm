def palindrome(n):
    for i in range(len(n) // 2):
        if n[i] != n[-i-1]:
            return False
    return True

while True:
    N = input()
    if N == '0':
        break
    if palindrome(N):
        print('yes')
    else:
        print('no')