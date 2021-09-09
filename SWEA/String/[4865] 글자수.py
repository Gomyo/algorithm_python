# Using my_dict
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    my_dict = {}
    for i in str2:
        if my_dict.get(i) != None:
            my_dict[i] += 1
        else:
            my_dict[i] = 1

    res = 0
    for i in str1:
        if my_dict.get(i) > res:
            res = my_dict.get(i)

    print(f'#{tc} {res}')

'''
# Using Counter
from collections import Counter

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    counter = Counter(str2)
    res = 0
    for i in str1:
        if counter[i] > res:
            res = counter[i]

    print(f'#{tc} {res}')
'''