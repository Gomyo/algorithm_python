def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    less, equal, big = [], [], []
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i > pivot:
            big.append(i)
        else:
            equal.append(i)
    return quick_sort(less) + equal + quick_sort(big)

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    A_sorted = quick_sort(A)
    left = 0
    right = -1
    res = []
    for i in range(10):
        if i%2 == 0:
            res.append(A_sorted[right])
            right -= 1
        else:
            res.append(A_sorted[left])
            left += 1

    print(f'#{tc}', *res)
