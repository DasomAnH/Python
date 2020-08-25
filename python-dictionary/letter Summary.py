user_input = str(input('what is the word count for you?'))

histogram = {}

for letter in user_input:
    if letter not in histogram:
        histogram[letter] = 1
    else:
        histogram[letter] += 1

print(histogram)
