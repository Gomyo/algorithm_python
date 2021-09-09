'''
7 11
0 1 32
0 2 31
0 5 60
0 6 51
1 2 21
2 6 25
2 4 46
3 4 34
3 5 18
4 5 40
4 6 51
'''
def sort(arr,E):
    for i in range(E-1):
        for j in range(E-i-1):
            if arr[j][2] > arr[j+1][2]:
                arr[j],arr[j+1] = arr[j+1],arr[j]


def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])


def union(x,y):
    a = find_set(x)
    b = find_set(y)

    if a == b:
        return
    else:
        p[b] = a

def kruskal(data):
    # 최소 가중치 비용을 저장할 변수
    result = 0
    #1. 정렬
    sort(data, E)
    #2. 선택,만약에 사이클이 생기면 선택안함
    #2-1. 사이클이 생기는지 판단하기 : 서로소집합 이용하기
    mst = []
    #data를 하나씩 읽으면서 사이클이 생기는지 확인
    for i in range(E):
        if find_set(data[i][0]) == find_set(data[i][1]): continue
        union(data[i][0], data[i][1])
        mst.append((data[i][0], data[i][1]))
        result += data[i][2]

    return result

#Kruskal
#1. 가중치의 크기 순서대로 정렬
#2. 가중치가 작은 간선들을 하나씩 선택(간선에 포함되는 노드들이 MST에 포함)
#3. 만약에 간선들을 선택하다가, 사이클이 생기면 선택하지 않는다.
#4. 모든 노드들이 선택될 때 까지 반복
V, E = map(int,input().split())
data = list()
p = list(range(V))

for e in range(E):
    a,b,w = map(int,input().split())
    data.append((a,b,w))

res = kruskal(data)
print(res)