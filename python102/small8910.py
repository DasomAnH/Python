count = 0

while count <= 10:

    print(count)

    count = count + 1

#----8----#

count = 2

while count <= 8:
    print(count)

    count = count + 1

#----9----#

square = 1

while square <= 5:

    print("*****")

    square = square + 1

#------10-----#

square2 = int(input('How big is the square?'))

for i in range(0, square2):
    s_str = ''
    for j in range(0, square2):
        s_str = s_str + "*"
    print(s_str)
