from collections import deque
C, R = map(int, input().split())
data = [list(map(int, input().split())) for x in range(R)]
delta = [(1, 0), (0, 1)]
res = 1e9

def find():
    global res

    q = deque([(0,0,0,[(0,0)])])
    visited = [[0]*C for x in range(R)]
    while q:
        cr,cc,cd,cp = q.popleft()
        print(cp)
        if (cr,cc) == (R-1, C-1):
            if res > cd:
                res = cd
                return cp

        for dr, dc in delta:
            nr = cr + dr
            nc = cc + dc
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc]:
                np = cp
                np.append((nr,nc))
                q.append((nr,nc,cd+data[nr][nc],np))
                visited[nr][nc] = 1

path = find()
print(res)
print(path)
'''
4 4
0 3 5 1
1 1 1 5
1 50 20 10
1 50 5 0
4 4
0 3 5 1
1 2 3 5
1 2 1 3
1 9 1 0

18
0,0
1,0
1,1
1,2
1,3
2,3
3,3

6
0 0
1 0
2 0
2 1
2 2
3 2
3 3
'''