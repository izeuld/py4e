# Encapsulate this code in a function named count, and generalize it so that it accepts the string and the letter as arguments

def count(word, searched):
    count = 0
    for letter in word:
        if letter == searched:
            count = count + 1
    print(count)

# adding user input:
word = input('Enter word:')
searched = input('Enter letter:')

count(word, searched)
