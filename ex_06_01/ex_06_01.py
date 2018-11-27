# Traversal through a string with a while loop:
fruit = 'rambutan'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
    if index == len(fruit):
        print('Yummy!')

# Traversal through a string with a for loop:
for char in fruit:
    print(char)
print('Tasty!')

# Write a while loop that starts at the last character in the string and works its way backwards to the first character in the string, printing each letter on a separate line, except backwards.
index = len(fruit)
while index > 0:
    letter = fruit[index-1]
    print(letter)
    index = index - 1
print('Yuck!')
