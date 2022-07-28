import math
def timetoint(n):
    sum = 0
    time = n.split(":")
    a=0
    b=0
    a = (int(ord(time[0][0])) - int(ord('0'))) * 10
    a += int(ord(time[0][1])) - int(ord('0'))
    a *=60
    b = (int(ord(time[1][0])) - int(ord('0'))) * 10
    b += int(ord(time[1][1])) - int(ord('0'))
    sum = a+b
    return sum
fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

answer = [0] * len(records)
fee_array = {}
cars_parking = {}



a = 0
for car in records:
    if car.split()[1] in cars_parking:
        a = timetoint(car.split()[0]) - timetoint(cars_parking[car.split()[1]])
        if car.split()[1] in fee_array:
            fee_array[car.split()[1]] +=a
        else:
            fee_array[car.split()[1]] = a
        a=0
        del cars_parking[car.split()[1]]
        continue
    cars_parking[car.split()[1]] = car.split()[0]

for car in cars_parking.keys():
    a = timetoint('23:59') - timetoint(cars_parking[car])
    fee_array[car] +=a
fee_list = sorted(fee_array.items())

car_fee = [0] * len(fee_list)
for car in range(len(fee_list)):
    a = fee_list[car][1]
    if a <= 180:
        car_fee[car] = 5000
    else:
        car_fee[car] = 5000+math.ceil((a - 180) / 10) * 600



print(car_fee)