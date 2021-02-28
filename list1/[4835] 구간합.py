T = int(input())

def ft_sum(data):
    res = 0
    for i in data:
        res += i
    return res

for t in range(1, T + 1):
    n, m = map(int, input().split())
    nums = list(map(int, input().split()))

    max_val = 0
    min_val = ft_sum(nums[:m])

    for i in range(n - m + 1):
        cal = ft_sum(nums[i:i+m])
        if cal > max_val:
            max_val = cal
        elif cal < min_val:
            min_val = cal
    res = max_val - min_val

    print(f'#{t} {res}')

'''input
3
10 3
1 2 3 4 5 6 7 8 9 10
10 5
6262 6004 1801 7660 7919 1280 525 9798 5134 1821 
20 19
3266 9419 3087 9001 9321 1341 7379 6236 5795 8910 2990 2152 2249 4059 1394 6871 4911 3648 1969 2176
'''