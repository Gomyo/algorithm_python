def solution(board, skills):
    answer = 0
    n = len(board[0])
    oneline_board = []
    # 1차원 리스트로 변환
    for b in board:
        oneline_board.extend(b)
    print(oneline_board)

    for skill in skills:
        type, r1, c1, r2, c2, degree = skill[0],skill[1],skill[2],skill[3],skill[4],skill[5]
        spot = []
        for i in range(r1, r2):
            for j in range(c1, c2):
                spot.append(i)
    return answer

solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]], [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])