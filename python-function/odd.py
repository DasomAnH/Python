def odd(number):
    if(number % 2 == 1):
        return True
    else:
        return False


is_number_odd = odd(int(input('Enter a number:')))

if is_number_odd:
    print('numebr is odd!')
else:
    print('number is even!')
