def hanoi(l, m, r, n):
    if n == 1: # 마지막 한번만 움직일 때는
        res.append([l, r]) # 왼쪽 장대에서 오른쪽 장대로
    else:
        hanoi(l, r, m, n-1) # 왼쪽 창대에서 중간 창대로 재귀
        res.append([l, r])  # 왼쪽 장대에서 오른쪽 장대로 옮긴 다음에
        hanoi(m, l, r, n-1) # 가운데 장대에서 오른쪽 장대로 옮겨준다.
res = []
hanoi(1, 2, 3, int(input()))
print(len(res))
for a,b in res:
    print(a,b)

'''
hanoi(1,2,3,3)
1,3,2,2 -> recursion
    1,2,3,1 -> + 1,3
    + 1,2
    3,1,2,1 -> + 3,2
+ 1,3
2,1,3,2 -> recursion
    2,3,1,1 -> + 2,1
    + 2,3
    1,2,3,1 -> 1,3
'''
