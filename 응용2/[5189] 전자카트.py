import sys
sys.stdin = open('5189.txt')

T = int(input())

def backtrack(idx, val):
    global result

    if val >= result:
        return

    if idx == N and :
        if val < result:
            result = val
        return

    for i in range(N):
        if idx != i and not checked[i]:
            selected[idx] = i
            checked[i] = 1
            backtrack(idx+1, val+data[idx][i])
            checked[i] = 0

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for x in range(N)]
    selected = [None] * N
    checked = [0] * N
    result = 2147483647
    backtrack(0, 0)
    print(result)