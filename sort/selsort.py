def selection_sort(N, arr):
    # 최소값을 찾아 앞에서부터 챡챡 채우는 정렬
    for i in range(N):
        # 최소값, 최소값 인덱스 초기화. i를 사용한다.
        min_idx, min_val = i, arr[i]

        # 반복문을 돌면서 최소값을 탐색한다.
        for j in range(i+1, N):
            if min_val > arr[j]:
                min_val = arr[j]
                min_idx = j
        # 최소값을 배열의 맨 앞으로 박아 넣는다.
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        print(arr)
    # 결과를 리턴한다
    return arr

arr = [5,2,6,1,9,3,7,8,4]
print(arr)
print(selection_sort(9, arr))