def binarySearch(book, page):
    left = 1
    right = book
    cnt = 1 # Start at 1
    while left <= right:
        mid = (left + right)//2
        if mid == page:
            return cnt
        elif mid > page: # If mid is bigger than target
            right = mid # 여기서 1 빼면 안된다!!
            cnt += 1
        elif mid < page: # If mid is smaller than target
            left = mid
            cnt += 1
    # Search Failure. There's no failure in this case, but I added it.
    return -1

T = int(input())

# 테케 9/10인 이유는?
# book인데 인덱스로 취급했다 ㅠㅠ; -1을 빼준다.
for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    # P : Book's whole pages
    A = binarySearch(P, Pa)
    B = binarySearch(P, Pb)

    if A == B:
        print(f'#{tc} 0')
    elif A < B:
        print(f'#{tc} A')
    else:
        print(f'#{tc} B')

# 잘못된 문제. 무한 루프가 나는 테스트 케이스
# 아래처럼 찾고자 하는 페이지가 마지막 page일 경우
# 1
# 300 300 200
