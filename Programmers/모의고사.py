def solution(answers):
    answer = [[1,0],[2,0],[3,0]]
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]

    for idx, val in enumerate(answers):
        if val == one[idx%5]:
            answer[0][1] += 1
        if val == two[idx%8]:
            answer[1][1] += 1
        if val == three[idx%10]:
            answer[2][1] += 1

    answer = sorted(answer, key=lambda x: (-x[1], x[0]))

    maxVal = answer[0][1]
    result = []
    for a in answer:
        if a[1] == maxVal:
            result.append(a[0])
    return result