# write a function farhrenheit
def convert(fah):
    return (fah - 32) * 5/9


while True:
    f = int(input('what is the temperature today?'))
    try:
        print((f - 32) * 5/9)
    except:
        print('nevermind')


celsius = convert(f)
print(celsius)
