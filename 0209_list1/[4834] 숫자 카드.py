T = int(input())

for t in range(1, T + 1):
    num_count = [0] * 10

    N = int(input())
    num = int(input())

    # num = 49679
    while num > 0:
        num_count[num%10] += 1
        num //= 10

    max_cnt = 0
    max_val = 0

    # for val, cnt in enumerate(num_count):
    #
    #     if cnt >= max_cnt:
    #         max_cnt, max_val = cnt, val

    for i in range(N):
        if num_count[i] >= max_cnt:
            max_cnt, max_val = num_count[i], i
    print(f'#{t} {max_val} {max_cnt}')



'''input
3
5
49679
5
08271
10
7797946543

1 
1
49679
'''

'''output
#1 9 2
#2 8 1
#3 7 3
'''