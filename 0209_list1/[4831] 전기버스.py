T = int(input())
#
# def charge(step, dest, buses, bus_stop):
#     # It is possible? Start, End?
#     if (bus_stop[buses - 1] + step) < dest or step < bus_stop[0]:
#         return 0
#     # Check distance between bus stops
#     for i in range(1, buses):
#         if (bus_stop[i] - bus_stop[i - 1]) > k:
#             return 0
#     # if passed
#     res = 0
#     if buses < dest // step:
#         res = buses
#     else:
#         res = dest//step
#     if bus_stop[buses - 1] == dest:
#         res -= 1
#     return res

# 통과한 쉬운 방법
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
    # res = charge(k, n, m, bus_stop_data)
    res = charge(k, n, bus_stop_data)

    print(f'#{t} {res}')

'''input
3
3 10 5
1 3 5 7 9
3 10 5
1 3 7 8 9
5 20 5
4 7 9 14 17

2
10 10 10
1 2 3 4 5 6 7 8 9 10
3 9 5
1 3 5 7 9

1
3 9 5
1 3 5 7 9

# Counterexample 교수님거
1
3 10 4
1 4 5 8

# 문제에 없는 TC
1
3 10 4
4 5 7 9
'''

