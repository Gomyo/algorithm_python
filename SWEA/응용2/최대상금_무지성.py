import sys
sys.stdin = open('최대상금.txt')
T = int(input())

for tc in range(1, T+1):
    num, cnt = input().split()
    N = len(num)
    res = [0] * N
    cnt = int(cnt)

    for i in range(N):
        res[i] = num[i]

    sorted_res = sorted(res, reverse=True)

    # 선택정렬
    idx = 0
    # 최대값이 되거나 값 체크 인덱스가 N-1보다 작으면 break
    while res != sorted_res and idx < N-1 and cnt:
        idx_to_change = []
        lower_than_idx = 0
        max_val = max(map(int, res[idx+1:]))

        # 맨 앞의 값이 가장 클 경우 다음 숫자로 넘어가서 비교
        if int(res[idx]) > max_val:
            idx += 1
            continue

        # 비교할 숫자들 중, 맨 앞의 값보다 크거나 같은 값이 있다면 바꿀 idx에 추가
        for i in range(idx+1, N):
            if int(res[i]) >= max_val:
                idx_to_change.append(i)
            # 맨 앞의 값보다 작은 값이 있다면 변수 추가
            else:
                lower_than_idx += 1

        # 최대값에 해당하는 idx들만 남김
        max_val = 0
        final_idx_to_change = []
        for i in idx_to_change:
            if int(res[i]) >= max_val:
                final_idx_to_change.append(i)

        # 만약
        if len(final_idx_to_change) >= 3 and lower_than_idx:
            res[idx], res[final_idx_to_change[-1-min(lower_than_idx, len(final_idx_to_change), cnt)]] = res[final_idx_to_change[-1-min(lower_than_idx, len(final_idx_to_change), cnt)]], res[idx]
        elif final_idx_to_change:
            res[idx], res[final_idx_to_change[-1]] = res[final_idx_to_change[-1]], res[idx]
        cnt -= 1
        idx += 1


    # 중복된 값이 있는지 체크
    dup_idx = 0
    for i in range(N - 1):
        if res[i] == res[i + 1]:
            dup_idx += 1
            break

    # 남은 교환 횟수만큼 교환
    while cnt:
        if dup_idx:
            cnt -= 1
        else:
            res[-2], res[-1] = res[-1], res[-2]
            cnt -= 1

    print("#{} {}".format(tc, "".join(res)))