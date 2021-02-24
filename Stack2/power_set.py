N = 5
arr = [1, 2, 3, 4, 5]
#각 집합 요소가 부분집합에 포함되는지 표시하는 배열
selected = [0] * N

def power_set(idx):
    # 모든 인덱스에 대해서 부분집합 포함 여부를 결정
    if idx == N:
        # print(selected)
        for i in range(N):
            if selected[i]:
                print(arr[i], end=" ")
        print()
        return
    # 아직 결정 덜했다!
    # 내가 할 수 있는 모든 경우의 수를 모두 수행하기

    # idx에 해당하는 요소가 부분집합에 포함 되는지 / 아닌지 결정해서 각각 진행(stacking) 생각
    selected[idx] = 1
    power_set(idx + 1)
    selected[idx] = 0
    power_set(idx + 1)

power_set(0)