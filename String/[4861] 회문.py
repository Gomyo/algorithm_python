# Runtime Error
# 만약 행 순회로 안되면, data의 행렬 순서를 뒤바꾼 뒤
# 행 순회로 for문을 2차원까지만 한정하자.
# 데이터 리팩토링을 통해 통과!!

def row_search(data, N, M):
    # 행 순회
    for i in range(N):
        for j in range(N - M + 1):
            if data[i][j:j + M] == data[i][j:j + M][::-1]:
                return data[i][j:j + M]

# Time complexity is too high
def col_search(data, N, M):
    # 열 순회
    for j in range(N):
        for i in range(N - M + 1):
            res = []
            for c in range(10):
                res.append(data[i+c][j])
            if res == res[::-1]:
                return res

# data refactor로 통과!
def data_refactor(data, N):
    res = []
    for j in range(N):
        tmp = []
        for i in range(N):
            tmp.append(data[i][j])
        res.append(tmp)
    return res

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    # M의 길이인 회문을 찾아라
    data = [list(input()) for _ in range(N)]

    row_result = row_search(data, N, M)

    if row_result == None:
        data = data_refactor(data, N)
        row_result = row_search(data, N, M)

    print(f'#{tc} {"".join(row_result)}')

'''
1
10 10
GOFFAKWFSM
OYECRSLDLQ
UJAJQVSYYC
JAEZNNZEAJ
WJAKCGSGCF
QKUDGATDQL
OKGPFPYRKQ
TDCXBMQTIO
UNADRPNETZ
ZATWDEKDQF
1
10 10
WPMACSIBIK
STWASDCOBQ
AMOUENCSOG
XTIIGBLRCZ
WXVSWXYYVU
CJVAHRZZEM
NDIEBIIMTX
UOOGPQCBIW
OWWATKUEUY
FTMERSSANL
'''
