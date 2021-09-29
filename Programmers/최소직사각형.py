# def solution(sizes):
#     h, l = 0, 0
#     for size in sizes:
#         if min(size) > l:
#             l = min(size)
#         if max(size) > h:
#             h = max(size)
#     return l*h

# 위 로직을 한줄로
def solution(sizes):
    return max(max(x) for x in sizes) * max(min(x) for x in sizes)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))

