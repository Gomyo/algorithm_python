import sys
sys.stdin = open('prim_input.txt')

V, E = map(int, input().split())
INF = 1e9

#1. 가중치(간선)를 저장하는 인접행렬 생성, 값 입력하기
adj = [[INF]*V for x in range(V)]

for i in range(E):
    s,e,w = map(int, input().split())
    adj[s][e] = w
    adj[e][s] = w

def prim(start):
    result = 0

    weight = [INF]*V
    weight[start] = 0

    visited = [0]*V
    st = [-1]*V

    for _ in range(V):
        min_w = INF
        min_v = 0

        #search min val,node
        for i in range(V):
            if weight[i] < min_w and not visited[i]:
                min_w = weight[i]
                min_v = i

        result += min_w
        visited[min_v] = 1

        #renew edge
        for i in range(V):
            if adj[min_v][i] < weight[i] and not visited[i]:
                weight[i] = adj[min_v][i]
                st[i] = min_v

    return result

print(prim(0))