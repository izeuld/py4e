# slicing strings but not snakes - the operator returns the part of the string from the "n-th" character to the "m-th" character, including the first but excluding the last:
badger = 'africa snake'
print(badger[:])
print(badger[0:6])
print(badger[7:])

# len is a built-in function that returns the number of characters in a string:
fruit = 'orange'
# i can use len like this:
length = len(fruit)
print(length)
# or like this:
print(len('orange'))

# Since we started counting at zero, the six letters are numbered 0 to 5. To get the last character, you have to subtract 1 from length:
last = fruit[length-1]
print(last)

# Methods are effectively functions that are built into the object and are available to any instance of the object. The method "upper" takes a string and returns a new string with all uppercase letters. Instead of the function syntax: upper(word), it uses the method syntax: word.upper() -> dot notation
word = 'banana'
new_word = word.upper()
print(new_word)
# BANANA

# A method call is called an invocation, e.g. we invoke find on word and pass the letter we are looking for as a parameter:
word = 'banana'
index = word.find('a')
print(index)
# 1
