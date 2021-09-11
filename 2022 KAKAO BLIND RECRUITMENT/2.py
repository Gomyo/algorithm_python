def cal(n, k):
    result = ''

    while n > 0:
        n, mod = divmod(n, k)
        result += str(mod)
    return result[::-1]

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    i = 2
    while i*i <= n:
        if n%i == 0:
            return False
        else:
            i += 1
    return True

def solution(n, k):
    answer = 0
    base = cal(n, k)
    arr = base.split('0')

    for i in arr:
        if i != '':
            if is_prime(int(i)):
                answer += 1
    return answer

solution(437674, 3)
solution(110011, 10)