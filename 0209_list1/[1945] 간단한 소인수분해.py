T = int(input())
for t in range(1, T + 1):
    n = int(input())
    res_array = [0] * 5
    insu = [11, 7, 5, 3, 2]

    while n > 1:
        for i in range(5):
            if n%insu[i] == 0:
                n //= insu[i]
                res_array[i] += 1
    res = []
    for i in res_array[::-1]:
        res.append(str(i))

    print(f'#{t} {" ".join(res)}')