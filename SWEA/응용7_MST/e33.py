import sys
sys.stdin = open('하나로input.txt')
INF = float("inf")


def prim(s):
    w_list = [INF] * N  # 선택한 간선의 가중치를 저장하는 배열
    picked = [False] * N  # 섬이 결정되었는지 저장하는 배열

    # 초기화
    w_list[s] = 0
    result = 0

    for _ in range(N):
        # w_list에 있는 값 중 가장 작은 값을 갖고 있는 섬을 찾습니다.
        min_w = INF
        min_idx = -1
        for i in range(N):
            if not picked[i] and w_list[i] < min_w:
                min_w = w_list[i]
                min_idx = i
        # 찾은 섬을 방문표시합니다.
        picked[min_idx] = True
        result += min_w
        # 새로 찾은 섬을 바탕으로 가중치 리스트를 업데이트 합니다.
        p_idx = min_idx
        for i in range(N):
            new_w = adj[p_idx][i]
            w_list[i] = min(w_list[i], new_w)
            # if not picked[i] and new_w < w_list[i]:
            #     w_list[i] = new_w
        # print(w_list)
    return result


T = int(input())

for tc in range(1, T + 1):
    # N: 섬의 개수
    N = int(input())
    # X: 섬의 X 좌표 리스트
    # Y: 섬의 Y 좌표 리스트
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    # E: 환경 부담 세율 실수
    E = float(input())

    # 주어진 섬들의 좌표를 이용하여, 가중치를 값으로 갖는 인접행렬을 만들자
    adj = [[0] * N for _ in range(N)]
    for n1 in range(N - 1):
        for n2 in range(n1 + 1, N):
            w = ((X[n1] - X[n2]) ** 2) + ((Y[n1] - Y[n2]) ** 2)
            adj[n1][n2] = w
            adj[n2][n1] = adj[n1][n2]  # 무향 그래프이기 때문에

    # 생성한 인접 행렬을 이용해 트리를 만들어보자
    answer = prim(0)
    print(f"#{tc} {round(answer * E)}")