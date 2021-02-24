# 반복문을 이용. 선형시간 O(n)
def iterative_power(x, n):
    result = 1
    for i in range(1, n+1):
        result *= x
    return result

# 분할정복. O(logN)
def recursive_power(x, n):
    if n == 1: return x
    if n % 2 == 0:
        y = recursive_power(x, n // 2)
        return y * y
    else:
        y = recursive_power(x, n // 2)
        return y * y * x

# print(iterative_power(2, 300000))
print(recursive_power(2, 5))