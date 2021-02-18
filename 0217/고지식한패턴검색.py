p = 'is'
t = 'this is a'
m = len(p)
n = len(t)
def brute_force(p, t):
    i = 0
    j = 0
    # 시간복잡도 : O(MN)
    while j < m and i < n:
        print(i, j)
        if t[i] != p[j]:
            i -= j
            j = -1
        i += 1
        j += 1
    if j == m: return i - m
    else: return -1
print(brute_force(p, t))