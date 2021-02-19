T = int(input())

for tc in range(1, T+1):
    data = [list(input()) for x in range(5)]
    res = ['' for x in range(15)]

    for i in range(5):
        for j in range(len(data[i])):
            res[j] += data[i][j]

    print(f'#{tc} {"".join(res)}')

'''
2
ABCDE
abcde
01234
FGHIJ
fghij
AABCDD
afzz
09121
a8EWg6
P5h3kx
'''
