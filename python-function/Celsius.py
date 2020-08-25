# write a fuction Celsius
def convert(cel):
    return (cel * 9/5) + 32


while True:
    c = int(input('what is the temperature today?'))
    try:
        print((c * 9/5) + 32)
    except:
        print('nevermind')


fahrenheit = convert(c)
print(fahrenheit)
