N = 3 # 행의길이
M = 4 # 열의길이

arr = [[1,2,3,4],
       [5,6,7,8],
       [9,10,11,12]]

# 행 우선순위를 역으로 돌아보자
print('행 역')
for i in range(N):
    for j in range(M-1, -1, -1):
        print(arr[i][j])

# 열
print('열')
for j in range(M):
    for i in range(N):
        print(arr[i][j])

# 열 역
print('열 역')
for j in range(M):
    for i in range(N-1, -1, -1):
        print(arr[i][j])

# 지그재그 순회
print('ZigZag')
for i in range(N):
    for j in range(M):
        print(arr[i][j + (M-1-2*j) * (i % 2)])