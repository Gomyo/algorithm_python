import sys
from pprint import pprint
sys.stdin = open('방사선치료input.txt', 'r')

T = int(input())

def duplicate(arr):
    dup = [[0]*data_length for x in range(data_length)]
    for i in range(data_length):
        for j in range(data_length):
            dup[i][j] = arr[i][j]
    return dup

def heal(data, K):
    global res
    tmp_data = duplicate(data)
    for i in range(data_length):
        for j in range(data_length):
            if tmp_data[i][j]:
                if check(xray(tmp_data,i,j,K)) == M and K not in res:
                    res.append(K)
                    return True
            else:
                tmp_data = duplicate(data)
    return False

def xray(tmp_data, r, c, K):
    for i in range(r, r+K):
        for j in range(c, c+K):
            if i < data_length and j < data_length:
                tmp_data[i][j] = 0
    return tmp_data

def check(check_data):
    remain_check = set()
    for i in range(data_length):
        for j in range(data_length):
            if check_data[i][j]:
                remain_check.add(check_data[i][j])
    return len(remain_check)

for tc in range(1, T+1):
    # N개의 종양이 2차원 배열로 주어진다. 색칠하기라고 보면 됨
    N, M = map(int, input().split())
    # 결과 변수
    res = []

    zongyangs = [list(map(int, input().split())) for x in range(N)]
    # K 탐색 좌표를 (point_start, 0)으로 해보자.
    point_start = 300
    data_length = 0

    for i in zongyangs:
        if max(i) > data_length:
            data_length = max(i)

    # 전체 데이터
    data = [[0]*data_length for x in range(data_length)]

    # 종양 정보 data. 종양마다 수를 부여해야 나중에 종양이 몇개 남았는지 체크 가능하다.
    z_cnt = 1
    for zongyang in zongyangs:
        zongyang_x_s = zongyang[0]
        zongyang_x_e = zongyang[2]

        if zongyang_x_s > zongyang_x_e:
            zongyang_x_s, zongyang_x_e = zongyang_x_e, zongyang_x_s

        zongyang_y_s = zongyang[1]
        zongyang_y_e = zongyang[3]
        if zongyang_y_s > zongyang_y_e:
            zongyang_y_s, zongyang_y_e = zongyang_y_e, zongyang_y_s

        for i in range(zongyang_x_s, zongyang_x_e):
            for j in range(zongyang_y_s, zongyang_y_e):
                data[i][j] = z_cnt
        z_cnt += 1

    # 만약 치료하지 않아도 종양의 개수가 이미 맞는다면 그냥 0을 제출
    if check(data) == M:
        res = 0
    # 치료하기
    else:
        K = data_length
        while K >= 1:
            heal(data, K)
            K //= 2

    for i in res:
        i -= 1
        heal(data, i)

    print('#{} {}'.format(tc, min(res)))

'''
1
30 0
102 132 11 76
8 97 107 23
36 99 74 158
92 72 31 58
86 50 122 37
97 78 159 27
98 157 13 100
27 36 4 130
3 9 18 102
69 69 152 123
86 103 98 29
54 53 151 5
1 107 12 80
95 159 5 65
48 56 4 126
1 95 44 83
94 98 130 88
97 186 72 89
37 88 85 50
111 36 22 104
71 58 34 11
70 109 24 91
93 86 129 96
107 90 30 149
95 158 64 82
38 13 58 56
99 99 142 128
138 76 68 127
101 92 30 182
102 85 56 149
'''
