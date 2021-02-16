def cal(s):
    stack = ''
    for i in range(len(s)):
        # 연속되었을 경우에만 해당 부분 삭제
        if stack and stack[-1] == s[i]:
            return stack[:-1] + s[i+1:]
        stack += s[i]
    #연속된 부분이 없다면 return False
    return 0

T = int(input())

for tc in range(1, T+1):
    String = input()

    while cal(String):
        String = cal(String)

    res = len(String)

    print(f'#{tc} {res}')
