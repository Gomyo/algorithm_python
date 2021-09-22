import re
def solution(new_id):
    tmp = new_id
    # 1
    tmp = tmp.lower()
    # 2
    tmp = re.sub("[^a-z0-9_\-.]", "", tmp)
    # 3
    tmp = re.sub("\.{2,}", ".", tmp)
    # 4
    if tmp == '':
        tmp = 'a'
    if tmp[0] == '.':
        tmp = tmp[1:]
    if tmp == '':
        tmp = 'a'
    if tmp[-1] == '.':
        tmp = tmp[:len(tmp)-1]
    # 5
    if tmp == '':
        tmp = 'a'

    # 6
    if len(tmp) >= 16:
        tmp = tmp[:15]
    if tmp[-1] == '.':
        tmp = tmp[:len(tmp)-1]

    #7
    if len(tmp) <= 2:
        tmp += tmp[-1]*(3-len(tmp))
    return tmp

# 반례
solution("=.=")