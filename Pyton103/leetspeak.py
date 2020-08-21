str1 = input('Enter your message?')

str1 = str1.upper()

translation = ''

for index in str1:
    if index == 'A':
        translation += '4'

    elif index == 'E':
        translation += '3'

    elif index == 'G':
        translation += '6'

    elif index == 'I':
        translation += '1'

    elif index == 'O':
        translation += '0'

    elif index == 'S':
        translation += '5'

    elif index == 'T':
        translation += '7'

    else:
        translation += index

print(translation)