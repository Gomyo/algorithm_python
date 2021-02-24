#Quick sort
# 두 가지 부분으로 나뉘어 진다.
# 1. 파티션을 기준으로, 큰값과 작은값을 나누는 과정
# 2. 나뉘어진 부분을 각각 다시 Quick sort를 수행하는 과정
# arr : 대상 배열
# left : 퀵소트를 수행할 시작 인덱스
# right : 퀵소트를 수행할 마지막 인덱스
def quick_sort(arr,left,right):
    if left < right:    #범위가 역전되지 않았을 경우에 수행
        #파티션, pivot : 큰값과 작은값으로 나눈 인덱스
        pivot = partition(arr,left,right)
        #각 부분에 대해서 quick sort 수행
        #pivot보다 작은 부분에 대한 quick sort
        quick_sort(arr,left,pivot-1)
        # pivot보다 큰 부분에 대한 quick sort
        quick_sort(arr, pivot+1, right)

def partition(arr,left,right):
    i = left
    j = right
    #pivot의 위치를 가장 왼쪽 요소로 선정
    pivot = arr[left]

    while i < j:
        # i를 증가 시키면서 pivot보다 큰값을 찾음
        while i <= j and arr[i] <= pivot:
            i += 1
        #j 는 감소하면서 pivot보다 작은값을 찾음
        while i <=j and arr[j] > pivot:
            j -= 1
        #위치를 교환해주면 되는데....
        if i < j:   # 위치가 역전되어 있으면, 제대로 된 교환이 아님
            arr[i],arr[j] = arr[j],arr[i]
    #j가 가리키는 인덱스 : 작은값들 중에서 제일 뒤에 있는 값
    #arr[j] 와 pivot의 위치를 바꿔주면 pivot이 자기 위치를 찾음
    arr[j], arr[left] = arr[left],arr[j]
    return j

arr = [8,7,6,5,4,3,2]
N = 7
quick_sort(arr,0,N-1)
print(arr)

# My Code
def my_quick_sort(arr):
    if len(arr) == 0:
        return arr
    pivot = arr[len(arr)//2]
    l, m, r = [], [], []
    for i in arr:
        if i < pivot:
            l.append(i)
        elif i > pivot:
            r.append(i)
        else:
            m.append(i)
    return my_quick_sort(l) + m + my_quick_sort(r)

