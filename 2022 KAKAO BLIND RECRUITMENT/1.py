def solution(id_list, reports, k):
    answer = []

    ban_count = {}
    dup_ban_check = {}

    for user in id_list:
        ban_count[user] = 0
        dup_ban_check[user] = []

    for report in reports:
        # a: 신고한 유저
        # b: 신고된 유저
        a, b = report.split(' ')
        if b not in dup_ban_check[a]:
            ban_count[b] += 1
            dup_ban_check[a].append(b)

    banned = {}
    for key, val in ban_count.items():
        if val >= k:
            banned[key] = True

    # id 리스트의 길이 <= 1000
    # dup_ban_check[user]의 최대 길이 <= 999
    for user in id_list:
        mail = 0
        for banned_user in dup_ban_check[user]:
            if banned.get(banned_user) is not None:
                mail += 1
        answer.append(mail)
    return answer

# 2,1,1,0
solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2)
# 0,0
solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)