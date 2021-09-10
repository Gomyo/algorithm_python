def solution(weights, head2head):
    # tuple = winrate, heavier, weight, prev
    cal = []
    for i in range(len(weights)):
        n = head2head[i].count('N')
        w = head2head[i].count('W')
        l = head2head[i].count('L')
        if n != len(weights):
            winrate = w/(w+l)
        else:
            winrate = 0
        heavier = 0
        for j in range(len(weights)):
            if weights[i] < weights[j] and head2head[i][j] == 'W':
                heavier += 1
        cal.append((winrate, heavier, weights[i], i+1))
    answer = sorted(cal, key=lambda x: (-x[0], -x[1], -x[2], x[3]))
    answer = [x[3] for x in answer]
    return answer

# solution([50,82,75,120], ["NLWL","WNLL","LWNW","WWLN"])
solution([145, 92, 86], ["NWW", "LNW", "LLN"])
