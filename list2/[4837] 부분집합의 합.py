def ft_sum(data):
    res = 0
    for i in data:
        res += i
    return res

# A : set (1 ~ 12)
A = [x for x in range(1, 13)]
n = len(A)

# 모든 부분집합 리스트
subset_list = []

for i in range(1<<n): # 비트연산으로 부분집합의 개수 구하기
    tmp_list = []
    for j in range(n): # 원소의 수만큼 비트 비교
        if i&(1<<j): # i의 j번째 비트가 1이면 j번째 원소 출력
            tmp_list.append(A[j])
    subset_list.append(tmp_list)

T = int(input())

for tc in range(1, T+1):
    # N : Number of Elements 1 ~ 12
    # K : Sum of Elements 1 ~ 100
    N, K = map(int, input().split())

    res = 0

    for subset in subset_list:
        if len(subset) == N:
            if ft_sum(subset) == K:
                res += 1

    print(f'#{tc} {res}')

