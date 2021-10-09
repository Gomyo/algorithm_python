from collections import deque
from copy import deepcopy
def solution(n, queries):
    answer = []
    p = 0
    count = 0
    front = 0
    qq = deque([])
    Q = []
    for i in range(n):
        Q.append(deepcopy(qq))

    for command, number in queries:
        if command == -1:
            if count == 1:
                answer.append(front)
                count -= 1
            else:
                for i in range(n):
                    p = (p+1)%n
                    if len(Q[p]) != 0:
                        answer.append(front)
                        front = Q[p].popleft()
                        p = (p+1)%n
                        break
        else:
            if count == 0:
                front = number
            else:
                Q[command].append(number)
            count += 1
    return answer

print(solution(4, [[0,1], [0,2], [0,3], [3,4], [1,5], [1,6], [3,7], [2,8], [1,9], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1], [-1, -1],[-1, -1], [2,10], [-1, -1], [1,11], [-1, -1], [2,12], [-1, -1],[-1, -1]]))
