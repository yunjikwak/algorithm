N, K = map(int, input().split())

def C(n, k):
    if k == 0 or n == k:
        return 1
    return C(n-1, k) + C(n-1, k-1)

print(C(N,K))