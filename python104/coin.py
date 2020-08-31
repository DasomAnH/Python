
coin = int(input('How many coin do you have?'))

while True:
    if coin == 0:
        print(f'You have {coin} coin.')
    elif coin <= 1:
        print(f'You have {coin} coins.')
    else:
        print('Do you want another <y/n> ?')
        break
