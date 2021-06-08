def hunt(turn, monster, monster_cnt, attack, skill, skill_number):
    global min_turn

    # 현재 몬스터 구분
    if monster[monster_cnt] <= 0:
        monster_cnt += 1

    # 종료조건
    if monster_cnt == len(monster):
        if min_turn > turn:
            min_turn = turn
        return

    if min_turn < turn:
        return

    # 일반공격, 특수공격
    monster[monster_cnt] -= attack
    hunt(turn + 1, monster, monster_cnt, attack, skill, skill_number)
    monster[monster_cnt] += attack

    if skill_number > 0:
        monster[monster_cnt] -= skill
        skill_number -= 1
        hunt(turn + 1, monster, monster_cnt, attack, skill, skill_number)
        monster[monster_cnt] += skill

tc = int(input())
for t in range(1, tc + 1):
    # 일반공격, 특수공격, 특수공격 사용가능 횟수
    attack, skill, skill_number = map(int, input().split())
    # 몬스터의 체력정보가 담겨있는 리스트
    monster = list(map(int, input().split()))

    min_turn = 987654321
    hunt(0, monster, 0, attack, skill, skill_number)
    print("#{} {}".format(t, min_turn))

'''
input
9
3 5 2
5 6 8
2 7 1
21 4 9
4 6 11
9 34 45
7 10 5
21 28 30
3 16 1
4 22 35
9 17 3
44 43 15
2 19 4
37 36 4 28 39 19 21
4 18 6
37 40 45 22
3 14 6
34 32 39 30 5

output
#1 5
#2 15
#3 17
#4 10
#5 17
#6 9
#7 58
#8 16
#9 26
'''