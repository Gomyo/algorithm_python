n = int(input())

result = []

for i in range(1, n + 1):
    clap = 0
    w = str(i)

    if '3' in w:
        clap += w.count('3')
        w.replace('3', '')
    if '6' in w:
        clap += w.count('6')
        w.replace('6', '')
    if '9' in w:
        clap += w.count('9')
        w.replace('9', '')
    if clap == 0:
        result.append(w)
    else:
        result.append('-'*clap)

print(' '.join(result))
