num = 0

while True:
    try:
        num = int(input('Give me a number:'))
        if (num == 7):
            raise TypeError('I like 7')
        break
    except ValueError:
        print('please try again.')
    except TypeError:
        print('yo, lucky 7!')

print(f"you entered {num}")
