def sleep_or_work(day):
    if day == 0 or day == 6:
        return 'sleep in'
    else:
        return 'Go to work'


while True:
    day = int(input("day(0-6)?"))
    message = sleep_or_work(day)
    print(message)
