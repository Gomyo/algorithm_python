# T = int(input())
#
# arr = [[0 for x in range(T)] for y in range(T)]
#
# dr = [0, 1, 0, -1]
# dc = [1, 0, -1, 0]
# direction = 0
# cnt = 1
# go = T
# r, c = 0, 0
#
# for i in range(2*T-1):
#     if direction == 0:
#         for j in range(go):
#             arr[r][c] = cnt
#             cnt += 1
#             c += dc[direction]
#         c -= 1 # 다음 칸으로 이동해 있어야 하므로 (1, 4) 값 변환
#         r += 1 # 1 올려줌
#         go -= 1
#         direction = (direction+1)%4
#     elif direction == 1:
#         for j in range(go):
#             arr[r][c] = cnt
#             cnt += 1
#             r += dr[direction]
#         r -= 1 # 아래쪽으로 가다가 왼쪽으로 가야하므로 둘다 줄인다
#         c -= 1
#         direction = (direction+1)%4
#     elif direction == 2:
#         for j in range(go):
#             arr[r][c] = cnt
#             cnt += 1
#             c += dc[direction]
#         c += 1 # 왼쪽으로 가다가 위쪽으로 가야하므로 c 하나 더해주고
#         r -= 1
#         go -= 1
#         direction = (direction+1)%4
#     elif direction == 3:
#         for j in range(go):
#             arr[r][c] = cnt
#             cnt += 1
#             r += dr[direction]
#         r += 1
#         c += 1
#         direction = (direction+1)%4
#
# for i in arr:
#     for j in i:
#         print('%3d' %j, end=" ")
#     print()

# 교수님 코드

# arr = [[0] * 5 for _ in range(5)]
# N = 5
# cnt = 1
# # 특정조건일 때 계속 반복 : while
# # 반복 횟수가 정해져 있으면  for : 배열의 길이만큼, 요소의 개수만큼
# #모든 칸이 숫자로 채워질 때 까지 반복
# total = N*N
# #r,c는 숫자를 입력하려고 하는 좌표값
# r = 0
# c = 0
# dr = [0,1,0,-1]
# dc = [1,0,-1,0]
# direction = 0 # 시작 방향이 오른쪽이니까 0부터 시작
# #좌측 상단에서 시작, (0,0) 에서 시작
# while cnt <= total:
#     if 0 <= r < N and 0 <= c < N and not arr[r][c]:
#         arr[r][c] = cnt
#         cnt += 1
#     else: #방향이동이 필요함
#         r -= dr[direction]
#         c -= dc[direction]
#         direction = (direction + 1) % 4
#     #숫자 넣었으니 이동, 현재 이동방향으로 변화량 더하기
#     r += dr[direction]
#     c += dc[direction]
#     # print("!!!!!")

# #출력 부분
# for i in range(N):
#     for j in range(N):
#         # arr[i][j] = cnt
#         # cnt += 1
#         print(arr[i][j],end = " ")
#     print()

t = int(input())
arr = [[0 for x in range(t)] for y in range(t)]
cnt = 1
r = 0
c = 0
total = t*t
dr = [0,1,0,-1]
dc = [1,0,-1,0]
dd = 0
while cnt <= total:
    if 0 <= r < t and 0<= c < t and not arr[r][c]:
        arr[r][c] = cnt
        cnt += 1
    else:
        r -= dr[dd]
        c -= dc[dd]
        dd = (dd + 1) % 4
    r += dr[dd]
    c += dc[dd]
print(arr)
