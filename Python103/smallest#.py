numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

count = 0
small_num = 0

for ck_num in numbers:
    if ck_num <= small_num:
        small_num = ck_num
    print(small_num)
