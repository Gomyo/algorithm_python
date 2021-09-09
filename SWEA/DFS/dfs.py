# 1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7
# 인접행렬(adjacency matrix)을 이용해서 그래프 표현이 가능
# 정점의 개수  : 7
# 간선의 개수 :  8
V = 7
E = 8
edges = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
# 인접행렬은 인덱스의 번호를 정점의 번호와 매칭시켜서 사용
# 정점이 1번부터 시작이라면, 정점의 개수보다 1더큰 크기의 인접행렬을 사용
adj = [[0] * (V + 1) for _ in range(V + 1)]
# 2개의 정점정보가 한 쌍이니까 2개씩 읽어옴
for i in range(0, E * 2, 2):
    s = edges[i]
    e = edges[i + 1]
    adj[s][e] = 1
    adj[e][s] = 1


# 해야할일 이제 인접행렬 가지고 DFS 수행하기
# DFS 구현법 : 1. 반복문과 stack을 이용함, 2. 재귀를 이용함
def dfs(v):
    stack = list()
    # 한 번 방문한 노드를 재 방문하지 않기 위해서 표시하는 배열
    # 각 인덱스 노드 번호가 됨, 방문안했으면 0,방문했으면 1
    visited = [False] * (V + 1)
    stack.append(v)
    visited[v] = True
    print(v) #방문순서를 확인하기 위한 출력

    # 스택이 비어있지 않을 때까지 아래를 반복
    while stack:
        # 스택의 탑에 위치한 정점을 확인
        top = stack[-1]
        # 해당 정점에서 갈 수 있는 경로가 있는가??

        # 갈 수 있는 경로가 있으면 stack에 push
        # 인접행렬의 top 행을 순회
        for i in range(1, V+1):
            # i번 정점과 이어져있고 방문하지 않았으면
            if adj[top][i] == 1 and not visited[i]:
                # 갈 수 있는 정점
                stack.append(i)
                visited[i] = True # i번 노드를 방문 했음
                print(i, end=" ")
                break # 경로 찾았으면 즉시 해당 경로로 이동하기 위해서 break
        # 경로가 없으면 pop
        else: #for문 속 if에 걸리는 경우가 없을 경우 = 경로가 없음
            stack.pop()

def dfs3(v):
    stack = list()
    visited = [False] * (V+1)
    stack.append(v)
    visited[v] = True

    # 위 방법이랑 다른 점은, 한 정점에 방문하면 해당 정점에서 방문할 수 있는 모든 정점을 스택에 넣어준다는 것.
    # 해당 정점은 재방문할 필요가 없음
    # 숫자가 큰 노드부터 방문하게 된다.
    while stack:
        # 그때그때 빼버림
        top = stack.pop()
        print(top, end=" ")
        # top에서 갈 수 있는 모든 정점을 스택에 넣는다
        for i in range(1, V+1):
            if adj[top][i] and not visited[i]:
                stack.append(i)
                visited[i] = True

dfs(1)
print()
dfs3(1)