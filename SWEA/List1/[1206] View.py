T = 10 # 고정
def ft_max(list):
    max_val = 0
    for i in list:
        if max_val < i:
            max_val = i
    return max_val

def sun(list):
    if ft_max(list) == list[2]:
        return list[2] - ft_max(list[:2] + list[3:])
    else:
        return 0

# 열개의 테스트 케이스
for t in range(1, T + 1):
    n = int(input())
    aparts = list(map(int, input().split()))
    res = 0
    for i in range(2,len(aparts) - 2):
        res += sun(aparts[i-2:i+3])
    print(f'#{t} {res}')

'''tc
100
0 0 225 214 82 73 241 233 179 219 135 62 36 13 6 71 179 77 67 139 31 90 9 37 93 203 150 69 19 137 28 174 32 80 64 54 18 0 158 73 173 20 0 102 107 48 50 161 246 145 225 31 0 153 185 157 44 126 153 233 0 201 83 103 191 0 45 0 131 87 97 105 97 209 157 22 0 29 132 74 2 232 44 203 0 51 0 244 212 212 89 53 50 244 207 144 72 143 0 0
'''
