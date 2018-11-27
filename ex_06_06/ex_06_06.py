# Read the documentation of the string methods at 'https://docs.python.org/library/stdtypes.html#string-methods'
# You might want to experiment with some of them to make sure you understand how they work. strip and replace are particularly useful. The documentation uses a syntax that might be confusing. For example, in find(sub[, start[, end]]), the brackets indicate optional arguments. So sub is required, but start is optional, and if you include start, then end is optional.
str = 'humble penguin'

caput = str.capitalize()
sum = str.count('e'[6:])
look = str.find('ble')
swap = str.replace('pen', 'le ')
tease = str.strip(' ')

print(caput,sum,look,swap,tease)
