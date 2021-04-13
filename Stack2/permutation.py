arr = [1, 2, 3]
N = len(arr)
selected = [0] * N # 결과들이 저장될 리스트
check = [0] * N # 해당 원소를 이미 사용했는지 안했는지 체크

def permutation(idx):
    if idx == N:
        print(selected)
    else:
        for i in range(N):
            if check[i] == 0:
                selected[idx] = arr[i] # 값을 사용해라
                check[i] = 1 # i번째 자리는 사용했음
                permutation(idx+1)
                check[i] = 0 # 다음 반복문을 위해 원상복귀 시켜주기
permutation(1)