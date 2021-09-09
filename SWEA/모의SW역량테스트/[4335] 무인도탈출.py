T = int(input())
N = int(input())
box = []

for tc in range(1, T+1):
    for _ in range(N):
        a, b, c = map(int, input().split())
        # 선택한 가로, 세로를 제외한 나머지 하나가 높이로 계산됨