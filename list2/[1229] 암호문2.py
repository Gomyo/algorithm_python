T = 10

for tc in range(1, T+1):
    N = int(input())
    pw = list(input().split())
    C = int(input())
    command = []
    data = input().split()

    i = 0
    while len(command) < C:
        stack = []
        if i == 0:
            stack.append(data[i])
            i += 1
        if data[i] in ['I', 'D']:
            stack.append(data[i])
            i += 1
        while i < len(data) and data[i] not in ['I', 'D']:
            stack.append(data[i])
            i += 1
        command.append(stack)

    for i in command:
        if i[0] == 'I':
            idx = int(i[1])
            pw = pw[:idx] + i[3:] + pw[idx:]
        else:
            idx = int(i[1])
            pw = pw[:idx] + pw[idx+int(i[2]):]

    print('#{}'.format(tc), *pw[:10])