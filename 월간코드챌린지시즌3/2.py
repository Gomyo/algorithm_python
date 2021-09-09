def solution(grids):
    answer = []
    # 경로를 기록하면서 이동하고, 이전에 이동했던 경로라면 컷
    # 이동 방향은 총 4개
    # 이동 파라미터는 (start, to, dir)
    # 만약 격자의 끝으로 넘어갈 경우, 도착 위치는 같은 행, 렬의 0 혹은 n-1

    # from, to의 형태로 딕셔너리 체크
    path = {}
    move = [(0,1,'R'), (1,0,'D'), (0,-1,'L'), (-1,0,'U')]
    lc, lr = len(grids[0]), len(grids)

    # 1= up, 2= right, 3= down, 4= left
    for r in range(lr):
        for c in range(lc):
            for d in move:
                isValid = True
                distance = 1
                dr, dc, dd, od = r+d[0], c+d[1], d[2], d[2]
                if dr < 0: dr = lr-1
                elif dr >= lr: dr = 0
                elif dc < 0: dc = lc-1
                elif dc >= lc: dc = 0

                while True:
                    # 시작부터 이동경로가 겹칠 때
                    if path.get((r,c,dr,dc,dd)) is not None and distance == 1:
                        isValid = False
                        break
                    # 좌회전
                    if grids[dr][dc] == 'L':
                        if dd == 'L':
                            m = move[1]
                        elif dd == 'R':
                            m = move[3]
                        elif dd == 'D':
                            m = move[0]
                        else:
                            m = move[2]
                    # 우회전
                    elif grids[dr][dc] == 'R':
                        if dd == 'L':
                            m = move[3]
                        elif dd == 'R':
                            m = move[2]
                        elif dd == 'D':
                            m = move[0]
                        else:
                            m = move[1]
                    # 직진일 경우
                    else:
                        if dd == 'L':
                            m = move[2]
                        elif dd == 'R':
                            m = move[0]
                        elif dd == 'D':
                            m = move[1]
                        else:
                            m = move[3]
                    # 위치 이동 계산
                    nr, nc = dr+m[0], dc+m[1]
                    # 경로의 끝인지 계산
                    if nr < 0: nr = lr-1
                    elif nr >= lr: nr = 0
                    elif nc < 0: nc = lc-1
                    elif nc >= lc: nc = 0

                    if (dr,dc,nr,nc,dd) == (r,c,dr,dc,od):
                        print(dr,dc,nr,nc,dd, '와', r,c,dr,dc,od)
                        break
                    # 반복문 중간에 이미 갔던 경로를 만난다면 중복되는 경로임
                    if path.get((dr,dc,nr,nc,dd)) is None:
                        path[(dr,dc,nr,nc,dd)] = 1
                        distance += 1
                        dr, dc, dd = nr, nc, m[2]
                    else:
                        isValid = False
                        break

                if isValid:
                    answer.append(distance)
    return answer

print(solution(["SL","LR"]))
print(solution(["S"]))
print(solution(["R","R"]))

'''
["SL","LR"]	[16]
["S"]	[1,1,1,1]
["R","R"]	[4,4]
'''
