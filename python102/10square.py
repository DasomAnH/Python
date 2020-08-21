#------10-----#

square2 = int(input('How big is the square?'))

for i in range(0, square2):
    s_str = ''
    for j in range(0, square2):
        s_str = s_str + "*"
    print(s_str)
