bill = int(input('Total bill amount?'))

level = (input('level of the sevice \'good, fair and bad\'?'))


if level == ('good'):
    tip_amount = (bill*20/100)
    print('Tip amout:', tip_amount)

elif level == ('fair'):
    tip_amount = (bill*15/100)
    print('Tip amout:', tip_amount)
elif level == ('bad'):
    tip_amount = (bill*10/100)
    print('Tip amout:', tip_amount)

else:
    print('we can\'t finsh.man!')

tip_amount = int(tip_amount)
total = (bill + tip_amount)


print(f'your total is {total}$.')

per = int(input('How many people?'))

total1 = (total/per)

print('Amount per person for $', total1)
