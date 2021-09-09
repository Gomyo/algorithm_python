def selection_sort_recursion(arr, cnt):

    if cnt == len(arr):
        return arr

    for i in range(cnt, len(arr)):
        if arr[i] < arr[cnt-1]:
            arr[cnt-1], arr[i] = arr[i], arr[cnt-1]

    return selection_sort_recursion(arr, cnt+1)

print(selection_sort_recursion([5,4,3,2,1], 0))