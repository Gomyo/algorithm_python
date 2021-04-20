T = int(input())

def is_promising(x):
    for i in range(x):
        if selected[x] == selected[i] or abs(selected[x]-selected[i]) == (x-i):
            return False
    return True

def queen(cnt):
    global res

    if cnt == N:
        res += 1
        return
    for i in range(N):
        selected[cnt] = i
        if is_promising(cnt):
            queen(cnt+1)

for tc in range(1, T+1):
    N = int(input())
    res = 0
    selected = [0]*N
    queen(0)
    print('#{} {}'.format(tc, res))