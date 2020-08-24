numbers = [10, 20, 30, 99, 50, 12, 87, 90, 1, 101, 9182691, 12, -11, 42]

count = 0


def odd(number):
  if(number % 2 == 1):
    return True
  else:
    return False


is_number_odd = odd(int(input('Enter a number:'))

if is_number_odd:
    print('number is odd!')
else:
    print('number is even!')
