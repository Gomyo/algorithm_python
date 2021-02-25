T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 돌아가야 할 학생수
    comeback = [list(map(int, input().split())) for x in range(N)]

    # 방은 1 ~ 400까지
    # 경로가 겹치는 것의 의미
    # 1 -> 2  3 -> 6. 1->1 2->3 #안겹침
    # 1 -> 4  3 -> 6. 1->2 2->3 #겹침
    # 1 -> 6  3 -> 4. 1->3 2->2 #겹침
    # 실패.
    # [1,3] [4,6]이라면 답이 2여야 되는데 내 코드로는 1이 나온다.
    # 1, 3과 4, 6 각각이 어떤 복도를 쓰는지 쓰자. 같은 복도를 공유한다는 조건을 이걸로 해결하면 된다.
    # 복도 arr에 어떤 복도를 쓰는지 적어두자
    # 겹치는 복도가 있으면 시간을 늘리면 된다
    # 1은 1번 복도, 2는 1번 복도, 3은 2번 복도, 4는 2번 복도
    # (n+1)//2
    hallway = [0] * 201
    for time in comeback:
        s = (time[0]+1)//2
        e = (time[1]+1)//2
        if s > e:
            s, e = e, s
        for i in range(s, e+1):
            hallway[i] += 1
    res = 0
    for h in hallway:
        if h > res:
            res = h

    print('#{} {}'.format(tc, res))
'''
3  
4  
10 20 
30 40
50 60
70 80
2 
1 3
4 6
3
10 100
20 80
30 50
'''