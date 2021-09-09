data = [1, 2, 1, 3, 2, 4, 2, 5, 4, 6, 5, 6, 6, 7, 3, 7]
N = 7
adj = [[] for x in range(N+1)]

for i in range(0, len(data), 2):
    s = data[i]
    e = data[i+1]
    adj[s].append(e)
    adj[e].append(s)

def dfs(s):
    visited = [0]*(N+1)
    stack = [s]
    result = [s]
    # stack에는 지나온 정점을 넣어주는데,
    # stack의 top에 있는 요소가 현재 방문위치

    # stack에 있는 모든 정점 방문
    # 만약 해당 정점에서 갈 수 있는 경로가 없으면 pop
    while stack:
        top = stack[-1]
        visited[top] = 1

        for i in adj[top]:
            if not visited[i]:
                stack.append(i)
                result.append(i)
                break
        # for-else : for문이 break없이 모두 수행되었을때 수행
        else:
            stack.pop()

    return result


print(dfs(1))
