# pivot의 위치를 반환, 함수 실행뒤에는 전체가 pivot을 기준으로 큰 값과 작은 값으로 분리
def hoare_partition(arr, start, end):
    pivot = arr[start]
    i, j = start, end
    while i <= j:
        while arr[i] <= pivot:
            i += 1
        while arr[j] >= pivot:
            i -= 1
        if i < j:
            arr[i], arr[j] = arr[j], arr[i]
    arr[start], arr[j] = arr[j], arr[start]
    return j

def quick_sort(arr, start, end):
    if start >= end:
        return
    pivot = hoare_partition(arr, start, end)
    quick_sort(arr, start, pivot-1)
    quick_sort(arr, pivot+1, end)
    pass