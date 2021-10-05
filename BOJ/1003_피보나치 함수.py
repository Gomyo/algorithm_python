T = int(input())

def fibo_zero(n):
    if n <= 1:
        return 1-n
    if memo_zero[n]:
        return memo_zero[n]
    if memo_zero[n-1] and memo_zero[n-2]:
        memo_zero[n] = memo_zero[n-1] + memo_zero[n-2]
        return memo_zero[n]
    memo_zero[n] = fibo_zero(n-1) + fibo_zero(n-2)
    return fibo_zero(n-1) + fibo_zero(n-2)

def fibo_one(n):
    if n <= 1:
        return n
    if memo_one[n]:
        return memo_one[n]
    if memo_one[n-1] and memo_one[n-2]:
        memo_one[n] = memo_one[n-1] + memo_one[n-2]
        return memo_one[n]
    memo_one[n] = fibo_one(n-1) + fibo_one(n-2)
    return fibo_one(n-1) + fibo_one(n-2)

memo_zero = [0]*41
memo_one = [0]*41

for tc in range(T):
    N = int(input())
    print(f'{fibo_zero(N)} {fibo_one(N)}')

