N = 20 # 새콤달콤 개수

queue = [(1,0)]

# (0,0 [0] : 사람 번호, [1] : 직전까지 받았던 마이0의 개수

new_people = 1
last_people = 0

while N > 0:
    num, cnt = queue.pop(0)
    last_people = num # 마지막으로 받으러 온 사람
    cnt += 1 # 이번에 받을 새콤달콤의 수

    N -= cnt
    new_people += 1
    queue.append((num, cnt)) # 맨 뒤로가서 다시 주서기
    queue.append((new_people, 0)) # 새로운 사람도 줄섬
    print(queue)

print(last_people)