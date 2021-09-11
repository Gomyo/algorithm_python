answer = [-1]
high_difference = 0


def dfs(shot_arr, shot_cnt, shot_idx, score, peach, peach_score):
    global high_difference
    global answer

    stack = [(shot_arr, shot_cnt, shot_idx, score, peach, peach_score)]
    while stack:


    # dfs 종료
    if shot_idx == 11:
        difference = score - peach_score

        if score <= 0:
            return

        if difference <= 0:
            return

        shot_arr[10] += shot_cnt

        if difference >= high_difference:
            high_difference = difference
            # answer = shot_arr
            answer.append(shot_arr)
            print(answer, ',남은 화살: ', shot_cnt, ',라이언 스코어: ', score, ',어피치 스코어: ', peach_score, ',라이언 과녁: ', shot_arr, '차이: ', difference, '현재 최고 차이: ', high_difference)
        return

    # 어피치가 화살을 맞추는데 성공한 과녁이라면
    if peach[shot_idx] > 0:
        # 라이언이 해당 과녁에 어피치가 맞춘 화살보다 더 많이 보유하고 있으면 쏘거나 안쏘고 지나감
        if shot_cnt - peach[shot_idx] > 0:
            # 쏘면 라이언 점수
            shot_arr[shot_idx] = peach[shot_idx] + 1 # 어피치보다 한 발 더 쏘기
            dfs(shot_arr, shot_cnt - (peach[shot_idx] + 1), shot_idx+1, score+10-shot_idx, peach, peach_score)
            # 안쏘면 어피치 점수
            shot_arr[shot_idx] = 0
            dfs(shot_arr, shot_cnt, shot_idx+1, score, peach, peach_score+10-shot_idx)
        # 화살이 부족하다면 라이언은 0발, 그냥 어피치 점수
        else:
            shot_arr[shot_idx] = 0
            dfs(shot_arr, shot_cnt, shot_idx+1, score, peach, peach_score+10-shot_idx)
    # 어피치가 화살을 맞추는데 실패했다면
    else:
        # 라이언이 화살 있으면 쏘고 점수를 가져가거나, 안 쏘고 지나감
        if shot_cnt > 0:
            shot_arr[shot_idx] = 1
            dfs(shot_arr, shot_cnt-1, shot_idx+1, score+10-shot_idx, peach, peach_score)
            shot_arr[shot_idx] = 0
            dfs(shot_arr, shot_cnt, shot_idx+1, score, peach, peach_score)
        # 화살 없으면 안쏘고 지나감
        else:
            shot_arr[shot_idx] = 0
            dfs(shot_arr, shot_cnt, shot_idx+1, score, peach, peach_score)

def solution(n, info):
    global answer
    # recursive dfs
    arr = [0] * 11
    dfs(arr, n, 0, 0, info, 0)
    print(answer)
    return answer

solution(5, [2,1,1,1,0,0,0,0,0,0,0])
print()
solution(9, [0,0,1,2,0,1,1,1,1,1,1])
print()
solution(10, [0,0,0,0,0,0,0,0,3,4,3])