def madlib(name, subject):
    return f"{name}'s favorite subject is {subject}."


while True:
    name = input('what is your name?')
    subject = input('what is your favorite subject?')
    text = madlib(name, subject)
    print(text)
