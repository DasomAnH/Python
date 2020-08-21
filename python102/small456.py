day_of_week = int(input("day(0-6)?"))

if day_of_week == 1:
    print('monday')

elif day_of_week == 2:
    print('Tuesday')

elif day_of_week == 3:
    print('Wednesday')

elif day_of_week == 4:
    print('Thursday')

elif day_of_week == 5:
    print('Friday')

elif day_of_week == 6:
    print('Saturday')

else:
    print('sunday')

#--5--#

if day_of_week <= 5:
    print('go to work')

else:
    print('sleep in')

#--6--#

C = int(input('Temperture in Celsius?'))

F = ((C) * 9 / 5) + 32

print(F, 'F')
