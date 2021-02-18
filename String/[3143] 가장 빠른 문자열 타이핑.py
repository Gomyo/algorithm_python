T = int(input())
for i in range(1, T+1):
    a, b = input().split()
    b_len = a.count(b)
    a = a.replace(b, '')
    print(f'#{i} {len(a) + b_len}')