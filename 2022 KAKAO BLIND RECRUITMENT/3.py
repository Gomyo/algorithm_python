import math

def cal_time(s, e):
    sh, sm = s.split(':')
    eh, em = e.split(':')
    start = int(sh)*60 + int(sm)
    end = int(eh)*60 + int(em)
    return end - start

def solution(fees, records):
    car = {}
    car_fee = {}

    for record in records:
        time, car_num, in_out = record.split(' ')
        if in_out == 'IN':
            car[car_num] = time
        else:
            fee = cal_time(car[car_num], time)
            if car_fee.get(car_num) is None:
                car_fee[car_num] = fee
            else:
                car_fee[car_num] += fee
            del car[car_num]

    # 모든 순회가 끝나고도 car dictionary에 남아 있는 key의 출차 시간은 23:59
    for car_num, val in car.items():
        fee = cal_time(val, '23:59')
        if car_fee.get(car_num) is None:
            car_fee[car_num] = fee
        else:
            car_fee[car_num] += fee

    df_time, df_fee, unit_time, unit_fee = fees[0], fees[1], fees[2], fees[3]

    car_fee_arr = []

    for car_num, time in car_fee.items():
        car_fee_arr.append((car_num, time))

    car_fee_arr.sort(key=lambda x: x[0])

    # 마지막 계산
    answer = []

    for el in car_fee_arr:
        if el[1] < df_time:
            answer.append(df_fee)
        else:
            answer.append(math.ceil((el[1] - df_time)/unit_time) * unit_fee + df_fee)
    return answer

solution([180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"])