T = int(input())
for tc in range(1,T+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    res = 0

    for i in b:
        start = 0
        end = n-1
        flag = 0
        while start <= end:
            mid = (start+end)//2
            if a[mid] == i:
                res += 1
                break
            elif a[mid] > i:
                if flag == 1: break
                flag = 1
                end = mid-1
            else:
                if flag == 2: break
                flag = 2
                start = mid+1
    print('#{} {}'.format(tc, res))
