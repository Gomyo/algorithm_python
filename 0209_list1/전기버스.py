T = int(input())
def charge(step, dest, data):
    # Start step don't need electricity
    cur = step
    start = 0
    bus_stop = [0] * (dest + 1)
    res = 0
    # Create bus_stop data
    for i in data:
        bus_stop[i] = 1

    while cur < dest:
        # If current position is bus stop
        if bus_stop[cur] == 1:
            res += 1
            start = cur
            cur += step
        else:
            cur -= 1
            # If current position become start position, there's no charge
            if cur == start:
                return 0
    return res

for t in range(1, T + 1):
    k, n, m = map(int, input().split())
    bus_stop_data = list(map(int, input().split()))

    res = charge(k, n, bus_stop_data)

    print(f'#{t} {res}')
