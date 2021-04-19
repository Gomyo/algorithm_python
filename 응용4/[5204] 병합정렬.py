import sys
sys.stdin = open('5204')

T = int(input())

def merge(left, right):
    global res
    ln, rn = len(left), len(right)
    tmp = []
    i, j = 0, 0

    if left[-1] > right[-1]:
        res += 1

    while i < ln and j < rn:
        if left[i] <= right[j]:
            tmp.append(left[i])
            i+=1
        else:
            tmp.append(right[j])
            j+=1

    while i < ln:
        tmp.append(left[i])
        i += 1

    while j < rn:
        tmp.append(right[j])
        j += 1

    return tmp


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    res = 0
    data = merge_sort(data)
    print('#{} {} {}'.format(tc, data[N//2], res))
