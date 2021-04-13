def check(arr):
    if ((arr[1]+arr[3]+arr[5]+arr[7])*3 + arr[0]+arr[2]+arr[4]+arr[6])%10:
        return False
    return True

T = int(input())
ratio_to_dec = {'112':0, '122':1, '221':2, '114':3, '231':4, '132':5, '411':6, '213':7, '312':8, '211':9}
hex_to_bin = {'0':'0000', '1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 'A':'1010', 'B':'1011', 'C':'1100', 'D':'1101', 'E':'1110', 'F':'1111'}

for tc in range(1, T+1):
    R, C = map(int, input().split())
    # 왜 슬라이싱으로 받아야 통과인가?
    lst = [input()[:C] for x in range(R)]

    # 열 중복 제거 (-2600ms)
    data = list(set(lst))
    R2 = len(data)

    # hex to bin
    bin_data = [''] * R2
    for i in range(R2):
        for c in data[i]:
            bin_data[i] += hex_to_bin[c]

    calculated = []
    answer = 0

    for i in range(R2-1, -1, -1):
        result = []
        d1 = d2 = d3 = 0
        # 1이 아예 없는 경우 배제 (-200ms)
        if '1' not in bin_data[i]:
            continue
        for j in range(C*4-1, -1, -1):
            if d2 == 0 and d3 == 0 and bin_data[i][j] == '1':
                d1 += 1
            elif d1 and d3 == 0 and bin_data[i][j] == '0':
                d2 += 1
            elif d1 and d2 and bin_data[i][j] == '1':
                d3 += 1

            if d3 and bin_data[i][j] == '0':
                gcd = min(d1, d2, d3)
                result.append(ratio_to_dec[str(d1//gcd) + str(d2//gcd) + str(d3//gcd)])
                d1 = d2 = d3 = 0

            if len(result) == 8:
                if result not in calculated:
                    if check(result):
                        answer += sum(result)
                    calculated.append(result)
                result = []

    print('#{} {}'.format(tc, answer))
