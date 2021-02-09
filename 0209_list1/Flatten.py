# import sys
# sys.stdin = open('Flatten.txt', 'r')

T = 10

'''
# Using Sort
for t in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))

    # 가로 길이는 항상 100
    for i in range(dump):
        boxes.sort()
        boxes[0] += 1
        boxes[99] -= 1
    boxes.sort()
    res = boxes[99] - boxes[0]
    print(f'#{t} {res}')
'''

def ft_diff(boxes):
    min_val = boxes[0]
    max_val = 0
    for i in boxes:
        if i < min_val:
            min_val = i
        elif i > max_val:
            max_val = i
    return max_val - min_val

def ft_dump(boxes):
    min_idx, min_val, max_idx, max_val = 0, boxes[0], 0, 0

    for i in range(len(boxes)):
        if boxes[i] <= min_val:
            min_idx, min_val = i, boxes[i]
        elif boxes[i] >= max_val:
            max_idx, max_val = i, boxes[i]
    return (min_idx, min_val, max_idx, max_val)

for t in range(1, T + 1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    min_idx = 0
    max_idx = 0

    while dump:
        min_idx, min_val, max_idx, max_val = ft_dump(boxes)
        boxes[min_idx] += 1
        boxes[max_idx] -= 1
        dump -= 1

    # 한번 더 깎기 전에 연산해야 하므로, val을 출력하자.
    # print(boxes[max_idx] - boxes[min_idx])
    min_idx, min_val, max_idx, max_val = ft_dump(boxes)
    res = max_val - min_val
    print(f'#{t} {res}')



'''input
834
42 68 35 1 70 25 79 59 63 65 6 46 82 28 62 92 96 43 28 37 92 5 3 54 93 83 22 17 19 96 48 27 72 39 70 13 68 100 36 95 4 12 23 34 74 65 42 12 54 69 48 45 63 58 38 60 24 42 30 79 17 36 91 43 89 7 41 43 65 49 47 6 91 30 71 51 7 2 94 49 30 24 85 55 57 41 67 77 32 9 45 40 27 24 38 39 19 83 30 42
669
93 26 56 35 50 42 13 46 61 19 54 40 24 80 97 88 30 50 38 67 50 94 96 98 17 87 6 89 83 56 35 15 2 17 72 87 64 14 56 86 54 13 9 33 46 14 57 22 59 47 83 82 45 97 23 30 62 36 51 74 67 45 60 93 40 54 25 55 11 46 50 87 14 75 23 69 19 88 6 59 92 3 26 78 15 15 25 35 75 73 60 34 71 88 98 19 78 74 71 64
'''

'''output
#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29
'''