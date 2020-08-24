def even(number):
    if (number % 2 == 0):
        return True
    else:
        return False


is_number_even = even(int(input('Enter a number:')))

if is_number_even:
    print('numebr is even!')
else:
    print('number is odd!')